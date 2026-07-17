#!/usr/bin/env python3
"""
Seed database with 5 hero heritage sites and sample data.
Run: python scripts/seed_database.py
"""
import asyncio
import uuid
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import engine, async_session_maker, init_db
from app.models.site import HeritageSite, ArtifactModel
from app.models.audio_asset import AudioAsset
from app.models.artisan import ArtisanPersona, KnowledgeChunk, ArtisanResponse


HERO_SITES = [
    {
        "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "name_vi": "Quan họ Bắc Ninh",
        "name_en": "Quan họ Folk Singing of Bắc Ninh",
        "description_vi": "Quan họ là thể loại dân ca đối đáp đặc trưng của vùng Kinh Bắc, được UNESCO công nhận là Di sản văn hóa phi vật thể đại diện của nhân loại năm 2009.",
        "description_en": "Quan họ is a distinctive antiphonal folk singing genre from the Kinh Bắc region, recognized by UNESCO as Intangible Cultural Heritage of Humanity in 2009.",
        "latitude": 21.1861,
        "longitude": 106.0763,
        "province": "Bắc Ninh",
        "district": "Thành phố Bắc Ninh",
        "heritage_type": "intangible",
        "unesco_status": "inscribed",
        "cultural_layers": ["quan_ho", "bac_ninh", "kinh_bac", "folk_singing", "unesco"],
        "cover_image": "/images/quan-ho-cover.jpg",
        "audio_preview": "/audio/quan-ho-preview.mp3",
        "artifact_model_id": "model-dan-bau",
    },
    {
        "id": "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        "name_vi": "Ca trù Hà Nội",
        "name_en": "Ca trù Singing of Hà Nội",
        "description_vi": "Ca trù là thể loại nghệ thuật diễn xướng phòng cổ truyền thống, được UNESCO công nhận là Di sản văn hóa phi vật thể cần được bảo vệ gấp năm 2009.",
        "description_en": "Ca trù is a traditional chamber music genre, recognized by UNESCO as Intangible Cultural Heritage in Need of Urgent Safeguarding in 2009.",
        "latitude": 21.0285,
        "longitude": 105.8542,
        "province": "Hà Nội",
        "district": "Hoàn Kiếm",
        "heritage_type": "intangible",
        "unesco_status": "inscribed",
        "cultural_layers": ["ca_tru", "ha_noi", "chamber_music", "unesco"],
        "cover_image": "/images/ca-tru-cover.jpg",
        "audio_preview": "/audio/ca-tru-preview.mp3",
        "artifact_model_id": "model-dan-nhi",
    },
    {
        "id": "c3d4e5f6-a7b8-9012-cdef-345678901234",
        "name_vi": "Nhã nhạc Huế",
        "name_en": "Nhuệ Court Music of Huế",
        "description_vi": "Nhã nhạc cung đình Huế là loại nhạc tộc truyền thống của Việt Nam, được UNESCO công nhận là Di sản văn hóa phi vật thể đại diện của nhân loại năm 2003.",
        "description_en": "Nhuệ court music is a traditional Vietnamese court music, recognized by UNESCO as Intangible Cultural Heritage of Humanity in 2003.",
        "latitude": 16.4637,
        "longitude": 107.5909,
        "province": "Thừa Thiên Huế",
        "district": "Thành phố Huế",
        "heritage_type": "intangible",
        "unesco_status": "inscribed",
        "cultural_layers": ["nha_nhac", "hue", "court_music", "unesco", "royal"],
        "cover_image": "/images/nha-nhac-cover.jpg",
        "audio_preview": "/audio/nha-nhac-preview.mp3",
        "artifact_model_id": "model-trong-de",
    },
    {
        "id": "d4e5f6a7-b8c9-0123-defa-456789012345",
        "name_vi": "Đờn ca tài tử",
        "name_en": "Đờn ca tài tử Music of Southern Vietnam",
        "description_vi": "Đờn ca tài tử là nghệ thuật âm nhạc truyền thống của người Nam Bộ, được UNESCO công nhận là Di sản văn hóa phi vật thể đại diện của nhân loại năm 2013.",
        "description_en": "Đờn ca tài tử is a traditional musical art form of Southern Vietnam, recognized by UNESCO as Intangible Cultural Heritage of Humanity in 2013.",
        "latitude": 10.0452,
        "longitude": 105.7469,
        "province": "Cần Thơ",
        "district": "Ninh Kiều",
        "heritage_type": "intangible",
        "unesco_status": "inscribed",
        "cultural_layers": ["don_ca_tai_tu", "mien_nam", "chamber_music", "unesco"],
        "cover_image": "/images/don-ca-tai-tu-cover.jpg",
        "audio_preview": "/audio/don-ca-tai-tu-preview.mp3",
        "artifact_model_id": "model-dan-tranh",
    },
    {
        "id": "e5f6a7b8-c9d0-1234-efab-567890123456",
        "name_vi": "Hò Nghệ An",
        "name_en": "Hò Work Songs of Nghệ An",
        "description_vi": "Hò là thể loại dân ca lao động phổ biến ở vùng Nghệ Tĩnh, phản ánh đời sống sinh hoạt, sản xuất của người dân nơi đây.",
        "description_en": "Hò is a work song folk genre popular in the Nghệ Tĩnh region, reflecting the daily life and production activities of local people.",
        "latitude": 18.6796,
        "longitude": 105.6927,
        "province": "Nghệ An",
        "district": "Thành phố Vinh",
        "heritage_type": "intangible",
        "unesco_status": "national",
        "cultural_layers": ["ho", "nghe_an", "work_songs", "labor", "national"],
        "cover_image": "/images/ho-nghe-an-cover.jpg",
        "audio_preview": "/audio/ho-nghe-an-preview.mp3",
        "artifact_model_id": "model-ao-dai",
    },
]

ARTIFACT_MODELS = [
    {
        "id": "model-dan-bau",
        "name_vi": "Đàn bầu",
        "name_en": "Đàn bầu (Monochord)",
        "description_vi": "Đàn bầu là nhạc cụ dây đơn đặc trưng của Việt Nam, tạo âm nhờ kỹ thuật nẩy, rung, lầy.",
        "description_en": "Đàn bầu is Vietnam's distinctive monochord, producing sound through bending, vibrato, and glissando techniques.",
        "model_url": "/models/dan-bau.glb",
        "scale": "0.5 0.5 0.5",
        "position": "0 0 -1",
    },
    {
        "id": "model-dan-nhi",
        "name_vi": "Đàn nhị",
        "name_en": "Đàn nhị (Two-string Fiddle)",
        "description_vi": "Đàn nhị là nhạc cụ dây hai dây, âm thanh ngân ngon, thường dùng trong Ca trù.",
        "description_en": "Đàn nhị is a two-string fiddle with clear sound, commonly used in Ca trù.",
        "model_url": "/models/dan-nhi.glb",
        "scale": "0.5 0.5 0.5",
        "position": "0 0 -1",
    },
    {
        "id": "model-trong-de",
        "name_vi": "Trống đế",
        "name_en": "Trống đế (Court Drum)",
        "description_vi": "Trống đế là trống lớn dùng trong Nhã nhạc cung đình, tạo âm thanh trầm, dồn dập.",
        "description_en": "Trống đế is a large drum used in Court Music, producing deep, resonant sounds.",
        "model_url": "/models/trong-de.glb",
        "scale": "0.5 0.5 0.5",
        "position": "0 0 -1",
    },
    {
        "id": "model-dan-tranh",
        "name_vi": "Đàn tranh",
        "name_en": "Đàn tranh (16-string Zither)",
        "description_vi": "Đàn tranh là nhạc cụ dây 16 dây, phổ biến trong Đờn ca tài tử.",
        "description_en": "Đàn tranh is a 16-string zither, common in Đờn ca tài tử music.",
        "model_url": "/models/dan-tranh.glb",
        "scale": "0.5 0.5 0.5",
        "position": "0 0 -1",
    },
    {
        "id": "model-ao-dai",
        "name_vi": "Áo dài",
        "name_en": "Áo dài (Traditional Dress)",
        "description_vi": "Áo dài là trang phục truyền thống của người Việt, gợi nhớ đến hình ảnh phụ nữ vùng Nghệ.",
        "description_en": "Áo dài is Vietnam's traditional dress, evoking images of Nghệ An women.",
        "model_url": "/models/ao-dai.glb",
        "scale": "0.5 0.5 0.5",
        "position": "0 0 -1",
    },
]

ARTISAN_PERSONAS = [
    {
        "id": "artisan-quan-ho-01",
        "name_vi": "Bà Nguyễn Thị Hương",
        "name_en": "Mrs. Nguyen Thi Huong",
        "birth_year": 1955,
        "region": "Bắc Ninh",
        "specialty": "quan_ho_singer",
        "bio_vi": "Bà Hương là nghệ nhân Quan họ gạo cội, đã dành trọn đời gắn bó với dòng ca Quan họ Bắc Ninh. Bà từng được phong tặng Nghệ nhân Ưu tú năm 2005.",
        "bio_en": "Mrs. Huong is a master Quan họ artisan who has dedicated her life to Bac Ninh Quan họ singing. She was awarded the title of Meritorious Artisan in 2005.",
        "avatar_url": "/images/artisan-huong.jpg",
        "voice_sample_url": "/audio/artisan-huong-intro.mp3",
    },
    {
        "id": "artisan-ca-tru-01",
        "name_vi": "Thầy Nguyễn Văn Mùi",
        "name_en": "Master Nguyen Van Mui",
        "birth_year": 1948,
        "region": "Hà Nội",
        "specialty": "ca_tru_master",
        "bio_vi": "Thầy Mùi là một trong những người giữ gìn nghệ thuật Ca trù cuối cùng, con trai của nghệ nhân Nguyễn Văn Đao. Thầy đã dạy truyền nghề cho nhiều thế hệ học trò.",
        "bio_en": "Master Mui is one of the last guardians of Ca trù art, son of artisan Nguyen Van Dao. He has taught many generations of students.",
        "avatar_url": "/images/artisan-mui.jpg",
        "voice_sample_url": "/audio/artisan-mui-intro.mp3",
    },
    {
        "id": "artisan-nha-nhac-01",
        "name_vi": "Nghệ nhân Mai Văn Biên",
        "name_en": "Artisan Mai Van Bien",
        "birth_year": 1952,
        "region": "Huế",
        "specialty": "nha_nhac_musician",
        "bio_vi": "Nghệ nhân Biên là người trực tiếp tham gia phục hồi Nhã nhạc Huế sau năm 1990, am hiểu عميق về các chế độ, bài nhạc cung đình.",
        "bio_en": "Artisan Bien directly participated in restoring Hue Court Music after 1990, with deep knowledge of court music modes and repertoire.",
        "avatar_url": "/images/artisan-bien.jpg",
        "voice_sample_url": "/audio/artisan-bien-intro.mp3",
    },
    {
        "id": "artisan-don-ca-01",
        "name_vi": "Bà Trần Thị Kim Loan",
        "name_en": "Mrs. Tran Thi Kim Loan",
        "birth_year": 1960,
        "region": "Cần Thơ",
        "specialty": "don_ca_tai_tu_singer",
        "bio_vi": "Bà Loan là ca sĩ Đờn ca tài tử nổi tiếng miền Tây, từng đoạt giải Nhất cuộc thi Đờn ca tài tử toàn quốc. Bà am hiểu các bài hát cổ, cách trình diễn.",
        "bio_en": "Mrs. Loan is a famous Southern Đờn ca tài tử singer, winner of National First Prize. She knows classical repertoire and performance practices.",
        "avatar_url": "/images/artisan-loan.jpg",
        "voice_sample_url": "/audio/artisan-loan-intro.mp3",
    },
    {
        "id": "artisan-ho-01",
        "name_vi": "Ông Lê Văn Tám",
        "name_en": "Mr. Le Van Tam",
        "birth_year": 1950,
        "region": "Nghệ An",
        "specialty": "ho_singer",
        "bio_vi": "Ông Tám là người lao động,xưởng gốm, cũng là ca sĩ Hò gạo cội. Ông biết nhiều câu Hò đập lúa, Hò giã gạo, Hò kéo còi.",
        "bio_en": "Mr. Tam is a potter and authentic Hò singer. He knows many work songs: rice pounding, rice winnowing, conch pulling Hò.",
        "avatar_url": "/images/artisan-tam.jpg",
        "voice_sample_url": "/audio/artisan-tam-intro.mp3",
    },
]

KNOWLEDGE_CHUNKS = [
    # Quan họ chunks
    {
        "site_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "artisan_persona_id": "artisan-quan-ho-01",
        "category": "history",
        "content_vi": "Quan họ hình thành từ thế kỷ 13, gắn liền với văn hóa làng xã Kinh Bắc. Theo lời người già, Quan họ bắt đầu từ các hội chè trầu, hội văn hóa nơi người trẻ tụ tập hát đòi, hát đối đáp.",
        "content_en": "Quan họ formed in the 13th century, linked to Kinh Bac village culture. Elders say it began at tea and betel gatherings where youth sang call-and-response.",
        "source_type": "interview",
        "verified_by": "Bà Nguyễn Thị Hương",
        "verified_at": "2024-01-15",
    },
    {
        "site_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "artisan_persona_id": "artisan-quan-ho-01",
        "category": "technique",
        "content_vi": "Kỹ thuật nẩy hát là đặc trưng nhất của Quan họ: giọng hát bật lên cao đột ngột rồi rơi xuống, tạo cảm xúc mạnh. Kỹ thuật này cần hơi thở tốt và kiểm soát thanh quang chính xác.",
        "content_en": "The nay hat technique is most characteristic of Quan họ: voice suddenly jumps high then falls, creating strong emotion. Requires good breath control and precise vocal fold control.",
        "source_type": "interview",
        "verified_by": "Bà Nguyễn Thị Hương",
        "verified_at": "2024-01-15",
    },
    {
        "site_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "artisan_persona_id": "artisan-quan-ho-01",
        "category": "meaning",
        "content_vi": "Trao trầu trong Quan họ không chỉ là lễ phép, mà là biểu tượng của tình cảm chân thành. Câu hát 'Trầu không phải trầu, trầu là lòng' thể hiện tinh thần này.",
        "content_en": "Betel offering in Quan họ is not just etiquette, but symbol of sincere affection. The lyric 'Betel is not betel, betel is the heart' expresses this spirit.",
        "source_type": "interview",
        "verified_by": "Bà Nguyễn Thị Hương",
        "verified_at": "2024-01-15",
    },
    # Ca trù chunks
    {
        "site_id": "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        "artisan_persona_id": "artisan-ca-tru-01",
        "category": "history",
        "content_vi": "Ca trù ra đời từ thế kỷ 11, ban đầu gọi là 'hát cửa đình' - hát ở cửa nhà thờ làng. Sau này vào cung đình và các hội quán, trở thành nghệ thuật phòng cung tinh tế.",
        "content_en": "Ca trù originated in the 11th century, initially called 'hat cua dinh' - singing at village communal house. Later entered court and guilds, becoming refined chamber art.",
        "source_type": "document",
        "verified_by": "Thầy Nguyễn Văn Mùi",
        "verified_at": "2024-01-10",
    },
    {
        "site_id": "b2c3d4e5-f6a7-8901-bcde-f23456789012",
        "artisan_persona_id": "artisan-ca-tru-01",
        "category": "technique",
        "content_vi": "Ca trù có 56 bài hát chính thức (bài thứ, bài nhiều...). Kỹ thuật 'ở' (giọng lắc) và 'ngăn' (giọng thẳng) là hai giọng chính. Phách đánh nhịp, đàn nhị kéo cung.",
        "content_en": "Ca trù has 56 official pieces. Techniques 'o' (vibrato voice) and 'ngan' (straight voice) are two main styles. Phach beats time, dan nhi bows.",
        "source_type": "interview",
        "verified_by": "Thầy Nguyễn Văn Mùi",
        "verified_at": "2024-01-10",
    },
    # Nhã nhạc chunks
    {
        "site_id": "c3d4e5f6-a7b8-9012-cdef-345678901234",
        "artisan_persona_id": "artisan-nha-nhac-01",
        "category": "ritual",
        "content_vi": "Nhã nhạc có 12 chế độ cung đình (Giao thiên, Tế tổ, Triều hội...). Mỗi chế độ có bài nhạc, nhịp, điều khắc quy định chặt chẽ theo Nho giáo.",
        "content_en": "Court music has 12 court modes (Heaven worship, Ancestor worship, Court audience...). Each mode has prescribed pieces, rhythms, rules per Confucian principles.",
        "source_type": "document",
        "verified_by": "Nghệ nhân Mai Văn Biên",
        "verified_at": "2024-01-12",
    },
    # Đờn ca tài tử chunks
    {
        "site_id": "d4e5f6a7-b8c9-0123-defa-456789012345",
        "artisan_persona_id": "artisan-don-ca-01",
        "category": "technique",
        "content_vi": "Đờn ca tài tử có 20 bài gốc (bài tố, bài nhạc...). Nghệ thuật immediate (sáng tác ngay) là đặc trưng: nghệ sĩ即兴 biến tấu trên khung bài cố định.",
        "content_en": "Don ca tai tu has 20 principal pieces. Improvisation is characteristic: artists spontaneously vary on fixed piece structures.",
        "source_type": "interview",
        "verified_by": "Bà Trần Thị Kim Loan",
        "verified_at": "2024-01-18",
    },
    # Hò Nghệ An chunks
    {
        "site_id": "e5f6a7b8-c9d0-1234-efab-567890123456",
        "artisan_persona_id": "artisan-ho-01",
        "category": "lyrics",
        "content_vi": "Hò Nghệ An có nhiều loại: Hò đập lúa, Hò giã gạo, Hò kéo còi, Hò hái chè. Lời hát thường 6-8 chữ, vần điệu tự nhiên, phản ánh lao động sản xuất.",
        "content_en": "Nghệ An Hò has many types: rice pounding, rice winnowing, conch pulling, tea picking. Lyrics typically 6-8 words, natural rhyme, reflecting production labor.",
        "source_type": "recording",
        "verified_by": "Ông Lê Văn Tám",
        "verified_at": "2024-01-20",
    },
]

PRE_RECORDED_RESPONSES = [
    {
        "persona_id": "artisan-quan-ho-01",
        "question_intent": "origin of quan ho",
        "question_vi": "Quan họ bắt nguồn từ đâu?",
        "question_en": "Where does Quan họ originate from?",
        "answer_vi": "Theo lời các bậc tiền bối, Quan họ hình thành từ thế kỷ 13 tại vùng Kinh Bắc, bắt đầu từ các hội chè trầu nơi người trẻ hát đối đáp.",
        "answer_en": "According to elders, Quan họ formed in the 13th century in the Kinh Bac region, starting from tea gatherings where youth sang call-and-response.",
        "audio_url_vi": "/audio/response-quan-ho-origin-vi.mp3",
        "audio_url_en": "/audio/response-quan-ho-origin-en.mp3",
        "confidence": 1.0,
        "citations": ["chunk-quan-ho-history"],
    },
    {
        "persona_id": "artisan-quan-ho-01",
        "question_intent": "why betel in quan ho",
        "question_vi": "Tại sao hát Quan họ phải trao trầu?",
        "question_en": "Why is betel exchanged in Quan họ?",
        "answer_vi": "Trầu trân là lễ nghĩa, biểu tượng của tình cảm chân thành. Câu hát 'Trầu không phải trầu, trầu là lòng' nói lên tất cả.",
        "answer_en": "Betel is etiquette, symbol of sincere affection. The lyric 'Betel is not betel, betel is the heart' says it all.",
        "audio_url_vi": "/audio/response-quan-ho-betel-vi.mp3",
        "audio_url_en": "/audio/response-quan-ho-betel-en.mp3",
        "confidence": 1.0,
        "citations": ["chunk-quan-ho-meaning"],
    },
    {
        "persona_id": "artisan-ca-tru-01",
        "question_intent": "ca tru instruments",
        "question_vi": "Ca trù dùng nhạc cụ gì?",
        "question_en": "What instruments are used in Ca trù?",
        "answer_vi": "Ca trù dùng phách (gõ nhịp), đàn nhị (kéo cung), và sáo (thỉnh thoảng). Ba nhạc cụ này tạo nên âm màu đặc trưng 'phách - nhị - sáo'.",
        "answer_en": "Ca trù uses phach (beat), dan nhi (bowed), and sao (flute occasionally). These three create the signature 'phach-nhi-sao' timbre.",
        "audio_url_vi": "/audio/response-ca-tru-instruments-vi.mp3",
        "audio_url_en": "/audio/response-ca-tru-instruments-en.mp3",
        "confidence": 1.0,
        "citations": ["chunk-ca-tru-technique"],
    },
    {
        "persona_id": "artisan-nha-nhac-01",
        "question_intent": "nha nhac modes",
        "question_vi": "Nhã nhạc có bao nhiêu chế độ?",
        "question_en": "How many modes does Court Music have?",
        "answer_vi": "Nhã nhạc cung đình có 12 chế độ chính, mỗi chế độ ứng với một nghi lễ cụ thể như Giao thiên, Tế tổ, Triều hội.",
        "answer_en": "Court Music has 12 principal modes, each corresponding to a specific ritual like Heaven Worship, Ancestor Worship, Court Audience.",
        "audio_url_vi": "/audio/response-nha-nhac-modes-vi.mp3",
        "audio_url_en": "/audio/response-nha-nhac-modes-en.mp3",
        "confidence": 1.0,
        "citations": ["chunk-nha-nhac-ritual"],
    },
    {
        "persona_id": "artisan-don-ca-01",
        "question_intent": "don ca tai tu improvisation",
        "question_vi": "Đờn ca tài tử có即兴 biểu diễn không?",
        "question_en": "Does Don ca tai tu have improvisation?",
        "answer_vi": "Có, nghệ thuật immediate (sáng tác ngay) là đặc trưng của Đờn ca tài tử. Nghệ sĩ即兴 biến tấu trên khung 20 bài gốc, thể hiện tài tình cá nhân.",
        "answer_en": "Yes, immediate improvisation is characteristic. Artists spontaneously vary on the 20 principal pieces, showing individual artistry.",
        "audio_url_vi": "/audio/response-don-ca-improv-vi.mp3",
        "audio_url_en": "/audio/response-don-ca-improv-en.mp3",
        "confidence": 1.0,
        "citations": ["chunk-don-ca-technique"],
    },
    {
        "persona_id": "artisan-ho-01",
        "question_intent": "ho nghe an types",
        "question_vi": "Hò Nghệ An có những loại nào?",
        "question_en": "What types of Nghe An Ho exist?",
        "answer_vi": "Hò Nghệ An có nhiều loại: Hò đập lúa, Hò giã gạo, Hò kéo còi, Hò hái chè... Mỗi loại gắn với một hoạt động lao động cụ thể.",
        "answer_en": "Nghệ An Ho has many types: rice pounding, rice winnowing, conch pulling, tea picking... Each links to a specific labor activity.",
        "audio_url_vi": "/audio/response-ho-types-vi.mp3",
        "audio_url_en": "/audio/response-ho-types-en.mp3",
        "confidence": 1.0,
        "citations": ["chunk-ho-lyrics"],
    },
]


async def seed_database():
    print("Initializing database...")
    await init_db()
    
    async with async_session_maker() as db:
        # Seed Artifact Models
        print("Seeding artifact models...")
        for model_data in ARTIFACT_MODELS:
            model = ArtifactModel(**model_data)
            db.add(model)
        
        # Seed Heritage Sites
        print("Seeding heritage sites...")
        for site_data in HERO_SITES:
            site = HeritageSite(**site_data)
            db.add(site)
        
        # Seed Artisan Personas
        print("Seeding artisan personas...")
        for persona_data in ARTISAN_PERSONAS:
            persona = ArtisanPersona(**persona_data)
            db.add(persona)
        
        # Seed Knowledge Chunks
        print("Seeding knowledge chunks...")
        for chunk_data in KNOWLEDGE_CHUNKS:
            chunk = KnowledgeChunk(**chunk_data)
            db.add(chunk)
        
        # Seed Pre-recorded Responses
        print("Seeding pre-recorded responses...")
        for resp_data in PRE_RECORDED_RESPONSES:
            resp = ArtisanResponse(**resp_data)
            db.add(resp)
        
        await db.commit()
        print("Database seeded successfully!")


if __name__ == "__main__":
    asyncio.run(seed_database())