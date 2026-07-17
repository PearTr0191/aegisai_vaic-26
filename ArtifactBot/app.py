"""
Museum Archive Chatbot — Flask API server
-----------------------------------------
Wraps the existing LangChain/Ollama RAG pipeline with a simple REST API so
the homepage chat widget can communicate with it over HTTP.

Start the server:
    python app.py

Endpoints:
    GET  /health   →  {"status": "online"|"initializing"|"error", "message": "..."}
    POST /chat     →  body: {"message": "..."} → {"response": "..."}
"""

import os
import threading

from flask import Flask, request, jsonify
from flask_cors import CORS

from langchain_community.document_loaders import Docx2txtLoader
from langchain_ollama import OllamaLLM as Ollama
from langchain_ollama import OllamaEmbeddings
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.vectorstores import Chroma
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# ── Flask app ─────────────────────────────────────────────────────────────────
app = Flask(__name__)
CORS(app)   # allow requests from index.html opened as a local file or any origin

# Global state — set by the background initializer thread
archive_bot    = None
bot_status     = "initializing"   # "initializing" | "online" | "error"
bot_status_msg = "Bot is loading, please wait a moment…"

WORD_FOLDER = "./artifacts_word_archive"

# ── RAG initializer (runs in a background thread so Flask starts instantly) ───
def _initialize():
    global archive_bot, bot_status, bot_status_msg

    try:
        if not os.path.exists(WORD_FOLDER):
            os.makedirs(WORD_FOLDER)
            bot_status     = "error"
            bot_status_msg = (f"Folder '{WORD_FOLDER}' created but is empty. "
                              "Add .docx artifact files and restart the server.")
            print(f"⚠️  {bot_status_msg}")
            return

        word_files = [f for f in os.listdir(WORD_FOLDER) if f.endswith('.docx')]
        if not word_files:
            bot_status     = "error"
            bot_status_msg = (f"No .docx files found in '{WORD_FOLDER}'. "
                              "Add your artifact Word documents and restart.")
            print(f"⚠️  {bot_status_msg}")
            return

        print(f"📂 Found {len(word_files)} Word file(s) — loading…")
        raw_documents = []
        for fn in word_files:
            loader = Docx2txtLoader(os.path.join(WORD_FOLDER, fn))
            raw_documents.extend(loader.load())

        print("🏛️  Connecting to local Ollama models…")
        llm        = Ollama(model="qwen2.5:7b", temperature=0.1, num_predict=140)
        embeddings = OllamaEmbeddings(model="qwen3-embedding:4b")

        print("📜 Semantic chunking…")
        splitter = SemanticChunker(embeddings, breakpoint_threshold_type="percentile")
        docs     = splitter.split_documents(raw_documents)
        print(f"✅ {len(docs)} semantic chunks indexed.")

        print("📦 Building Chroma vector store…")
        vector_store = Chroma.from_documents(docs, embeddings)
        retriever    = vector_store.as_retriever(search_kwargs={"k": 4})

        system_prompt = (
        "You are an expert museum curator and historian chatbot for our digital archive. "
        "Your mission is to provide engaging, accurate, and educational information about the "
        "historical artifacts in our collection using exclusively the provided context below.\n\n"
        "Guidelines:\n"
        "1. Maintain an authoritative, respectful, and engaging historical tone.\n"
        "2. Cite or mention the specific artifact's details accurately based on the text.\n"
        "3. If the user asks about an artifact or historical event not present in the provided context, "
        "politely respond: 'I am sorry, but that artifact or detail is not currently documented in our archive.'\n"
        "4. Do not invent or extrapolate historical facts outside of the given text.\n\n"
        "5. CRITICAL RULE: Keep your response brief, natural, and conversational. \n"
        "6. Limit your answer to a maximum of 2 to 3 sentences or roughly 50-60 words. \n"
        "7. Do not repeat entire paragraphs from the database.\n\n"
        "8. LANGUAGE MATCHING: Detect the language of the user's input (English or Vietnamese). "
        "You MUST answer in that exact same language TOTALLY. If the question is in Vietnamese, answer in Vietnamese. "
        "If it is in English, answer in English. Do not use both languages in an answer.\n"
        "9. If you do not understand the request, ask the user to inquire again.\n"
        "Collection Data Context:\n{context}"
        )
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])
        qa_chain    = create_stuff_documents_chain(llm, prompt)
        archive_bot = create_retrieval_chain(retriever, qa_chain)

        bot_status     = "online"
        bot_status_msg = f"Online — {len(docs)} artifact profiles loaded."
        print(f"🎉 {bot_status_msg}")

    except Exception as exc:
        bot_status     = "error"
        bot_status_msg = f"Initialization failed: {exc}"
        print(f"❌ {bot_status_msg}")


# ── Routes ────────────────────────────────────────────────────────────────────
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": bot_status, "message": bot_status_msg})


@app.route("/chat", methods=["POST"])
def chat():
    if bot_status == "initializing":
        return jsonify({
            "response": "The archive is still loading — please try again in a moment."
        }), 503

    if bot_status == "error":
        return jsonify({
            "response": f"The archive could not start: {bot_status_msg}"
        }), 503

    data    = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        return jsonify({"response": "Please enter a question."}), 400

    try:
        result = archive_bot.invoke({"input": message})
        return jsonify({"response": result.get("answer", "No answer returned.")})
    except Exception as exc:
        return jsonify({"response": f"An error occurred: {exc}"}), 500


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("🚀 Starting Museum Archive API…")
    threading.Thread(target=_initialize, daemon=True).start()
    app.run(host="0.0.0.0", port=5000, debug=False)

