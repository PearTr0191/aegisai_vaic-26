// VietHeritage Intangible Heritage Sites
// Merges with Project/VNMT.js TREASURES array

const INTANGIBLE_HERITAGE = [
  // ── QUAN HỌ BẮC NINH ──
  {
    id: 358,
    name: "Lễ hội Quan họ Bắc Ninh",
    english: "Quan Ho Bac Ninh Festival",
    location: "Đình Hồng, xã Hương Lâm, huyện Gây, Bắc Ninh",
    lat: 21.1861, lng: 106.0763,
    category: "intangible",
    badge: "UNESCO Intangible",
    type: "music",
    year: "Modern",
    desc: "Quan họ is a traditional folk singing style from Bắc Ninh province featuring call-and-response between male and female singers.",
    desc_vi: "Quan họ là dân ca đối đáp truyền thống của Bắc Ninh, hình thức biểu diễn chủ yếu là nam ca sĩ và nữ ca sĩ đối đáp nhau qua các câu hò.",
    audio_url: "/audio/quanho-preview.mp3"
  },
  {
    id: 359,
    name: "Đình Hồng - Nơi lưu giữ hồ sơ Quan họ",
    english: "Hong Temple - Quan Ho Archive Site",
    location: "Thành phố Bắc Ninh",
    lat: 21.1861, lng: 106.0763,
    category: "intangible",
    badge: "UNESCO Intangible",
    type: "ritual",
    year: "2014",
    desc: "The sacred temple where Quan họ melodies are preserved and performed during festivals.",
    desc_vi: "Đình Hồng là nơi lưu giữ và truyền lại các điệu Quan họ, nơi diễn ra các lễ hội truyền thống hàng năm.",
    audio_url: "/audio/quanho-ritual.mp3"
  },

  // ── CA TRÙ HÀ NỘI ──
  {
    id: 360,
    name: "Nhà ca - Nơi lưu giữ di sản Ca trù",
    english: "Traditional Ca tru House",
    location: "Hà Nội",
    lat: 21.0285, lng: 105.8542,
    category: "intangible",
    badge: "UNESCO Intangible",
    type: "music",
    year: "2009",
    desc: "Ca trù is a traditional Vietnamese form of chamber music performed with traditional instruments.",
    desc_vi: "Ca trù là một loại hình nghệ thuật diễn xướng truyền thống của Việt Nam, kết hợp giữa ca nhảy và nhạc cụ đờn, nhị, sao.",
    audio_url: "/audio/catu-preview.mp3"
  },

  // ── NHÃ NHẠC HUẾ ──
  {
    id: 361,
    name: "Nhã nhạc cung đình Huế",
    english: "Hue Royal Court Music",
    location: "Kinh thành Huế, Thừa Thiên Huế",
    lat: 16.4637, lng: 107.5909,
    category: "intangible",
    badge: "UNESCO Intangible",
    type: "music",
    year: "2003",
    desc: "The Hue Royal Court Music represents the musical traditions of the Nguyen Dynasty court.",
    desc_vi: "Nhã nhạc cung đình Huế là di sản tinh túy của triều đại nhà Nguyễn, biểu diễn sự uy nghi và thứ phái của hoàng gia.",
    audio_url: "/audio/nhuanhac-preview.mp3"
  },

  // ── ĐƠN CA TÀI TỨ CẦN THƠ ──
  {
    id: 362,
    name: "Đờn ca tài tử Nam Bộ",
    english: "Southern Don Ca Tai Tu Music",
    location: "Cần Thơ",
    lat: 10.0452, lng: 105.7469,
    category: "intangible",
    badge: "UNESCO Intangible",
    type: "music",
    year: "2012",
    desc: "Don ca tai tu is a traditional music form of southern Vietnam, combining vocal and instrumental performances.",
    desc_vi: "Đờn ca tài tử là nghệ thuật âm nhạc truyền thống của miền Tây Nam Bộ, phản ánh đời sống và tâm tưởng của người dân cảnh.",
    audio_url: "/audio/donantutu-preview.mp3"
  },

  // ── HÒ NGHỆ AN ──
  {
    id: 363,
    name: "Hò ca Nghệ An - Hò làng",
    english: "Nghe An Work Songs (Hò)",
    location: "Nghệ An",
    lat: 18.6796, lng: 105.6927,
    category: "intangible",
    badge: "National Intangible",
    type: "music",
    year: "Traditional",
    desc: "Traditional work songs from Nghệ An province, sung by farmers and laborers during harvests and fieldwork.",
    desc_vi: "Hò làng là các điệu dân ca lao động truyền thống của người nông dân Nghệ An, được hát trong quá trình làm việc và vui chơi.",
    audio_url: "/audio/ho-nghean-preview.mp3"
  }
];

// Combine with existing TREASURES
// Usage: TREASURES.push(...INTANGIBLE_HERITAGE);
// Or import via: const ALL_SITES = [...TREASURES, ...INTANGIBLE_HERITAGE];