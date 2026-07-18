/* ═══════════════════════════════════════
   ABOUT PAGE CONTENT DATA
   Structured for easy maintenance and bilingual support
═══════════════════════════════════════ */

// ── Page-level meta ──────────────────────────────────────────────
const ABOUT_META = {
  title: {
    vi: 'Giới thiệu — Bảo Vật Việt',
    en: 'About — Vietnam National Treasures'
  },
  pageEyebrow: {
    vi: 'Về dự án',
    en: 'About the Project'
  },
  pageTitleMain: {
    vi: 'Bảo Vật Việt',
    en: 'Vietnam National Treasures'
  },
  pageTitleSub: {
    vi: 'Kết nối quá khứ — Khơi dậy tương lai',
    en: 'Connecting the Past — Inspiring the Future'
  },
  pageDesc: {
    vi: 'Một kho lưu trữ số toàn diện về 357 bảo vật quốc gia Việt Nam — nơi di sản gặp gỡ công nghệ, và nơi mỗi hiện vật đều kể một câu chuyện值得 được chia sẻ.',
    en: 'A comprehensive digital archive of Vietnam\'s 357 national treasures — where heritage meets technology, and every artifact tells a story worth sharing.'
  }
};

// ── Intro section ────────────────────────────────────────────────
const INTRO_CONTENT = {
  heading: {
    vi: 'Bảo Vật Việt không chỉ là một trang web — đây là <strong class="highlight">kho lưu trữ số toàn diện</strong> về 357 bảo vật được công nhận là Bảo vật Quốc gia Việt Nam qua 14 đợt công nhận (tính đến năm 2025).',
    en: 'Vietnam National Treasures is not just a website — it is a <strong class="highlight">comprehensive digital archive</strong> of 357 artifacts recognized as Vietnam\'s National Treasures across 14 recognition rounds (as of 2025).'
  },
  paragraph: {
    vi: 'Từ những <strong>trống đồng Đông Sơn 4.000 năm tuổi</strong> đến <strong>bản thảo Sắc lệnh lập quốc năm 1945</strong>, hành trình này trải qua 6 nền văn minh, 165+ địa điểm, và 4 giai đoạn lịch sử trọng đại. Chúng tôi xây dựng nền tảng này với ba sứ mệnh cốt lõi:',
    en: 'From <strong>4,000-year-old Đông Sơn bronze drums</strong> to the <strong>1945 Independence Decree manuscript</strong>, this journey spans 6 civilisations, 165+ locations, and 4 major historical eras. We built this platform with three core missions:'
  },
  missions: [
    {
      icon: 'archive',
      title: {
        vi: 'Lưu trữ & Truy cập',
        en: 'Archive & Access'
      },
      desc: {
        vi: 'Tập trung dữ liệu phân tán thành một kho thống nhất, có thể tìm kiếm, lọc, và khám phá trực quan trên bản đồ tương tác.',
        en: 'Centralise scattered data into a unified, searchable, filterable, and visually explorable archive on an interactive map.'
      }
    },
    {
      icon: 'map-pin',
      title: {
        vi: 'Cầu nối số — Thực tế',
        en: 'Digital Bridge to Reality'
      },
      desc: {
        vi: 'Mỗi hiện vật trên màn hình đều gắn liền với một địa điểm thật. Chúng tôi muốn bạn <em>đi đến đó</em> — đến bảo tàng, đến di tích, đến làng nghề — để trải nghiệm di sản bằng mọi giác quan.',
        en: 'Every artifact on screen is tied to a real place. We want you to <em>go there</em> — to the museum, the heritage site, the craft village — to experience heritage with all your senses.'
      }
    },
    {
      icon: 'sparkles',
      title: {
        vi: 'Truyền cảm hứng',
        en: 'Inspire'
      },
      desc: {
        vi: 'Qua âm thanh, mô hình 3D, AI thủ công nghệ nhân, và kể chuyện đa phương tiện, chúng tôi biến dữ liệu khô khan thành hành trình cảm xúc.',
        en: 'Through sound, 3D models, artisan AI, and multimedia storytelling, we turn dry data into an emotional journey.'
      }
    }
  ]
};

// ── Values section ───────────────────────────────────────────────
const VALUES = [
  {
    icon: 'heart-handshake',
    title: {
      vi: 'Tôn trọng cộng đồng',
      en: 'Community Respect'
    },
    desc: {
      vi: 'Mọi dữ liệu đều xuất phát từ người地道 — nghệ nhân, trưởng lão, nhà nghiên cứu địa phương. Chúng tôi trích dẫn nguồn, xin phép, và chia sẻ quyền sở hữu.',
      en: 'All data originates from local people — artisans, elders, local researchers. We cite sources, seek permission, and share ownership.'
    }
  },
  {
    icon: 'shield-check',
    title: {
      vi: 'Chính xác & Minh bạch',
      en: 'Accuracy & Transparency'
    },
    desc: {
      vi: 'Phân biệt rõ ràng: dữ liệu chính thức (Chính phủ, UNESCO), nghiên cứu học thuật, và truyền thuyết địa phương. AI không được phép bịa đặt.',
      en: 'Clear distinction between official data (Government, UNESCO), academic research, and local legends. AI is not allowed to hallucinate.'
    }
  },
  {
    icon: 'globe',
    title: {
      vi: 'Mở & Bền vững',
      en: 'Open & Sustainable'
    },
    desc: {
      vi: 'Mã nguồn mở, dữ liệu có thể tải về, không khóa nền tảng. Thiết kế để chạy được 10 năm nữa không cần bảo trì phức tạp.',
      en: 'Open source, downloadable data, no vendor lock-in. Designed to run for 10+ years without complex maintenance.'
    }
  }
];

// ── Features section ─────────────────────────────────────────────
const FEATURES = [
  {
    icon: 'map',
    title: {
      vi: 'Bản đồ tương tác 357 điểm',
      en: 'Interactive Map of 357 Sites'
    },
    desc: {
      vi: 'Lọc theo thời kỳ, thể loại, trạng thái UNESCO. Click xem chi tiết, nghe âm thanh, xem mô hình 3D, hỏi AI.',
      en: 'Filter by era, genre, UNESCO status. Click for details, audio, 3D models, ask AI.'
    }
  },
  {
    icon: 'music',
    title: {
      vi: 'Kho âm thanh di sản',
      en: 'Heritage Sound Archive'
    },
    desc: {
      vi: '100+ đoạn âm thanh: trống đồng, cồng chiêng, ca trù, quan họ, xòe, bài chòi... Phân tích AI nhận diện thể loại, nhạc cụ, kỹ thuật trình diễn.',
      en: '100+ audio clips: bronze drums, gongs, ca trù, quan họ, xòe, bài chòi... AI analysis identifies genre, instruments, performance techniques.'
    }
  },
  {
    icon: 'box',
    title: {
      vi: 'Mô hình 3D hiện vật',
      en: 'Artifact 3D Models'
    },
    desc: {
      vi: 'Xem quay 360° trống Ngọc Lũ, ấn Hoàng đế chi bảo, xe tăng 390... Tải xuống mô hình để in 3D hoặc nghiên cứu.',
      en: '360° view of Ngọc Lũ drum, Imperial Seal, Tank 390... Download models for 3D printing or research.'
    }
  },
  {
    icon: 'bot',
    title: {
      vi: 'AI Bảo tàng — Hỏi đáp có nguồn',
      en: 'Museum AI — Sourced Answers'
    },
    desc: {
      vi: 'Hỏi về lịch sử, ý nghĩa, kỹ thuật. AI trả lời kèm trích dẫn: "Theo GS. Nguyễn Văn Huy, cuộc phỏng vấn 2019..." — nói "Tôi không biết" khi thiếu dữ liệu.',
      en: 'Ask about history, meaning, techniques. AI answers with citations: "Per Prof. Nguyễn Văn Huy, 2019 interview..." — says "I don\'t know" when data is missing.'
    }
  },
  {
    icon: 'layers',
    title: {
      vi: 'Lớp chuyện (Story Layers)',
      en: 'Story Layers'
    },
    desc: {
      vi: 'Bật/tắt các lớp truyện: "Câu chuyện kháng chiến", "Ca dao ru miền sông nước", "Nghề 궁廷" — khám phá di sản qua lăng kính văn hóa, không chỉ địa lý.',
      en: 'Toggle narrative layers: "Resistance Stories", "Delta Lullabies", "Court Crafts" — explore heritage through cultural lenses, not just geography.'
    }
  },
  {
    icon: 'download',
    title: {
      vi: 'Dữ liệu mở (Open Data)',
      en: 'Open Data Export'
    },
    desc: {
      vi: 'Tải CSV/GeoJSON toàn bộ 357 bảo vật: tọa độ, mô tả, hình ảnh, âm thanh, trạng thái UNESCO. Dùng cho nghiên cứu, giáo dục, ứng dụng thứ ba.',
      en: 'Download CSV/GeoJSON of all 357 treasures: coordinates, descriptions, images, audio, UNESCO status. For research, education, third-party apps.'
    }
  }
];

// ── Team / Credits ───────────────────────────────────────────────
const TEAM = [
  {
    initials: 'P1',
    name: {
      vi: 'Trưởng nhóm & Backend',
      en: 'Lead & Backend'
    },
    role: {
      vi: 'Kiến trúc hệ thống, API, triển khai, GPU orchestration',
      en: 'System architecture, API, deployment, GPU orchestration'
    },
    desc: {
      vi: 'Xây dựng FastAPI + SQLite-vec backend, Docker, Render/Netlify CI/CD, quản lý 15h GPU FPT AI Factory.',
      en: 'Built FastAPI + SQLite-vec backend, Docker, Render/Netlify CI/CD, managed 15h FPT AI Factory GPU.'
    }
  },
  {
    initials: 'P2',
    name: {
      vi: 'Frontend Lead — Bản đồ & Chi tiết',
      en: 'Frontend Lead — Map & Detail'
    },
    role: {
      vi: 'Leaflet, Waveform, 3D viewer, Mobile UX',
      en: 'Leaflet, Waveform, 3D viewer, Mobile UX'
    },
    desc: {
      vi: 'Bản đồ 5 điểm anh hùng, popup tùy chỉnh, waveform âm thanh, <model-viewer> 3D, responsive thiết kế di động.',
      en: '5 hero site map, custom popups, audio waveform, <model-viewer> 3D, mobile-responsive design.'
    }
  },
  {
    initials: 'P3',
    name: {
      vi: 'Frontend — AI & Trải nghiệm',
      en: 'Frontend — AI & Experience'
    },
    role: {
      vi: 'Chat UI, Audio Analyzer, i18n, Accessibility',
      en: 'Chat UI, Audio Analyzer, i18n, Accessibility'
    },
    desc: {
      vi: 'Giao diện Artisan Chat, kéo-thả phân tích âm thanh, chuyển đổi VI/EN, WCAG AA, bàn phím, screen reader.',
      en: 'Artisan Chat UI, drag-drop audio analyzer, VI/EN toggle, WCAG AA, keyboard nav, screen reader support.'
    }
  },
  {
    initials: 'P4',
    name: {
      vi: 'AI Lead — EthnoMusic Model',
      en: 'AI Lead — EthnoMusic Model'
    },
    role: {
      vi: 'CNN+BiLSTM, ONNX export, INT8 quantization',
      en: 'CNN+BiLSTM, ONNX export, INT8 quantization'
    },
    desc: {
      vi: 'Huấn luyện 8h: 5 thể loại, 12 nhạc cụ, 10 kỹ thuật trình diễn. Xuất ONNX INT8 chạy CPU <500ms trên Render free tier.',
      en: '8h training: 5 genres, 12 instruments, 10 techniques. ONNX INT8 export runs <500ms CPU on Render free tier.'
    }
  },
  {
    initials: 'P5',
    name: {
      vi: 'Dữ liệu & RAG-lite',
      en: 'Data & RAG-lite'
    },
    role: {
      vi: 'Seed data, Knowledge chunks, TTS, Embeddings',
      en: 'Seed data, Knowledge chunks, TTS, Embeddings'
    },
    desc: {
      vi: '5 hero sites JSON, 50 knowledge chunks VI/EN, Ollama vietnamese-bi-encoder, 10 TTS giọng nghệ nhân, few-shot prompts.',
      en: '5 hero sites JSON, 50 knowledge chunks VI/EN, Ollama vietnamese-bi-encoder, 10 artisan TTS voices, few-shot prompts.'
    }
  }
];

// ── Data Sources ─────────────────────────────────────────────────
const DATA_SOURCES = [
  {
    icon: 'government',
    title: {
      vi: 'Chính phủ Việt Nam — Thủ tướng Chính phủ',
      en: 'Government of Vietnam — Prime Minister'
    },
    desc: {
      vi: 'Quyết định công nhận 357 bảo vật quốc gia qua 14 đợt (2012–2025). Cơ sở dữ liệu chính thức, cập nhật lần cuối tháng 1/2025.',
      en: 'Decisions recognizing 357 national treasures across 14 rounds (2012–2025). Official database, last updated Jan 2025.'
    }
  },
  {
    icon: 'unesco',
    title: {
      vi: 'UNESCO — Di sản phi vật thể',
      en: 'UNESCO — Intangible Cultural Heritage'
    },
    desc: {
      vi: '16 di sản Việt Nam trong Danh sách đại diện & Cần bảo vệ khẩn cấp. Metadata: năm ghi danh, quốc gia, mô tả chính thức.',
      en: '16 Vietnamese inscriptions on Representative & Urgent Safeguarding Lists. Metadata: inscription year, country, official description.'
    }
  },
  {
    icon: 'university',
    title: {
      vi: 'Viện Nghiên cứu Văn hóa & Bảo tàng Quốc gia',
      en: 'Vietnam Institute of Culture & Arts Studies / National Museums'
    },
    desc: {
      vi: 'Hình ảnh, bản vẽ kỹ thuật, báo cáo khai quật, ghi âm thực địa. Cung cấp bởi Bảo tàng Lịch sử Quốc gia, Bảo tàng Dân tộc học, Viện Văn hóa Nghệ thuật.',
      en: 'Images, technical drawings, excavation reports, field recordings. Provided by Vietnam National Museum of History, Museum of Ethnology, VICAS.'
    }
  },
  {
    icon: 'user',
    title: {
      vi: 'Các nhà nghiên cứu độc lập & Cộng đồng',
      en: 'Independent Researchers & Community'
    },
    desc: {
      vi: 'Tiến sĩ Nguyễn Văn Huy, TS. Trần Văn Khê, nhóm Vietnam Heritage Hub, và hàng chục người yêu di sản đóng góp dữ liệu, âm thanh, hình ảnh.',
      en: 'Dr. Nguyễn Văn Huy, Dr. Trần Văn Khê, Vietnam Heritage Hub team, and dozens of heritage enthusiasts contributing data, audio, images.'
    }
  },
  {
    icon: 'map',
    title: {
      vi: 'OpenStreetMap & CartoDB',
      en: 'OpenStreetMap & CartoDB'
    },
    desc: {
      vi: 'Dữ liệu bản đồ nền, ranh giới tỉnh/huyện, tọa độ địa điểm — nguồn mở, cộng đồng cập nhật liên tục.',
      en: 'Base map tiles, province/district boundaries, location coordinates — open source, continuously updated by community.'
    }
  }
];

// ── Footer CTA ───────────────────────────────────────────────────
const FOOTER_CTA = {
  title: {
    vi: 'Sẵn sàng khám phá?<br><em>Hành trình 357 bảo vật bắt đầu từ một cú click.</em>',
    en: 'Ready to explore?<br><em>The journey of 357 treasures begins with a single click.</em>'
  },
  desc: {
    vi: 'Dù bạn là nhà nghiên cứu, học sinh, du khách, hay đơn giản là người yêu lịch sử — Bảo Vật Việt mở cửa cho mọi người. Vào bản đồ, chọn một hiện vật, và để câu chuyện bắt đầu.',
    en: 'Whether you\'re a researcher, student, traveler, or simply a history lover — Vietnam National Treasures opens its doors to all. Enter the map, choose an artifact, and let the story begin.'
  },
  buttons: {
    map: {
      vi: 'Mở bản đồ tương tác',
      en: 'Open Interactive Map'
    },
    database: {
      vi: 'Xem kho lưu trữ',
      en: 'Browse Archive'
    }
  }
};

// ── Navigation labels (shared with other pages) ──────────────────
const NAV_LABELS = {
  vi: {
    home: 'Trang chủ',
    map: 'Khám phá bản đồ',
    db: 'Kho lưu trữ',
    civs: 'Nền Văn Minh',
    about: 'Giới thiệu',
    mapBtn: 'Mở bản đồ'
  },
  en: {
    home: 'Home',
    map: 'Explore Map',
    db: 'Database',
    civs: 'Civilisations',
    about: 'About',
    mapBtn: 'Open Map'
  }
};

// ── Export all content as a single object ────────────────────────
const ABOUT_CONTENT = {
  meta: ABOUT_META,
  intro: INTRO_CONTENT,
  values: VALUES,
  features: FEATURES,
  team: TEAM,
  sources: DATA_SOURCES,
  footerCta: FOOTER_CTA,
  nav: NAV_LABELS
};

// Make available globally for about.html
window.ABOUT_CONTENT = ABOUT_CONTENT;