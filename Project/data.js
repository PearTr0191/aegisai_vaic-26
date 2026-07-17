/* ═══════════════════════════════════════
   UNESCO INTANGIBLE CULTURAL HERITAGE OF VIETNAM
   Shared dataset for the database / search page
   (data.js). Sourced from VNMT.js — keep in sync
   with the map page, which still inlines its own
   copy so VNMT.html keeps working standalone.

   Each entry describes one heritage item with:
     id, name (vi), english, lat, lng,
     location (display string), provinces (array),
     year (UNESCO recognition year, e.g. '2009'),
     status (inscribed | urgent | national | tentative),
     genre  (singings | instrumental | belief | festival),
     badge, desc_vi, desc.

   NOTE: There are NO individual markers and NO
   clusters on the map. Heritage is discovered by
   clicking a province, which opens a pie-chart
   modal listing the heritage it contains.
   Provinces are coloured by their heritage's
   dominant colour (status or genre dimension).
═══════════════════════════════════════ */
const TREASURES = [
  {
    id: 1,
    name: 'Quan họ Bắc Ninh',
    english: 'Quan họ Folk Singing of Bắc Ninh',
    lat: 21.1861, lng: 106.0763,
    location: 'Bắc Ninh · Vùng Kinh Bắc',
    provinces: ['Bắc Ninh'],
    year: '2009',
    status: 'inscribed',
    genre: 'singings',
    badge: 'UNESCO',
    desc_vi: 'Quan họ là thể loại dân ca đối đáp đặc trưng của vùng Kinh Bắc, được công nhận là Di sản văn hóa phi vật thể đại diện của nhân loại năm 2009. Ca hát diễn ra trong các lễ hội làng, bóng dáng thân thiện, mười câu mười lời trao gửi tình nghĩa trăm năm.',
    desc: 'Quan họ is an antiphonal folk singing genre from the Kinh Bắc region, inscribed on the UNESCO Representative List in 2009. Performed during village festivals, its gracious melodies and ten-verse exchanges express hundred-year bonds of friendship and affection.',
  },
  {
    id: 2,
    name: 'Ca trù',
    english: 'Ca trù (Hát Ả Đào) Chamber Singing',
    lat: 21.0285, lng: 105.8542,
    location: 'Hà Nội · Bách Khoa · Khâm Thiên',
    provinces: ['Hà Nội'],
    year: '2009',
    status: 'urgent',
    genre: 'singings',
    badge: 'UNESCO',
    desc_vi: 'Ca trù là thể loại nghệ thuật diễn xướng phòng cổ truyền thống, họa tiết phong phú, cách nhả chữ rung luyến tinh tế với đào nương, kép đàn và quan viên. UNESCO đưa vào Danh sách di sản cần bảo vệ khẩn cấp năm 2009.',
    desc: 'Ca trù is a complex form of sung chamber music with refined ornamentation, performed by a female singer (đào nương), lute player (kép đàn) and percussionist (quán viên). UNESCO inscribed it on the Urgent Safeguarding List in 2009.',
  },
  {
    id: 3,
    name: 'Nhã nhạc cung đình Huế',
    english: 'Huế Royal Court Music (Nhã nhạc)',
    lat: 16.4637, lng: 107.5909,
    location: 'Thừa Thiên Huế · Kinh đô Huế',
    provinces: ['Thừa Thiên Huế'],
    year: '2008',
    status: 'inscribed',
    genre: 'instrumental',
    badge: 'UNESCO',
    desc_vi: 'Nhã nhạc là âm nhạc cung đình Việt Nam, được biểu diễn trong các dịp lễ triều đình nhà Nguyễn tại Huế. Được UNESCO công nhận Di sản văn hóa phi vật thể đại diện của nhân loại năm 2008, là loại hình nghệ thuật âm nhạc truyền thống tinh tế bậc nhất.',
    desc: 'Nhã nhạc is Vietnamese court music performed at ceremonies of the Nguyễn dynasty in Huế. Inscribed on the UNESCO Representative List in 2008, it is among the most refined traditional musical art forms of Vietnam.',
  },
  {
    id: 4,
    name: 'Đờn ca tài tử',
    english: 'Đờn ca tài tử of Southern Vietnam',
    lat: 10.0452, lng: 105.7469,
    location: 'Cần Thơ · Đồng bằng sông Cửu Long',
    provinces: ['Cần Thơ','Hậu Giang','Sóc Trăng','Bạc Liêu','Cà Mau'],
    year: '2013',
    status: 'inscribed',
    genre: 'singings',
    badge: 'UNESCO',
    desc_vi: 'Đờn ca tài tử là nghệ thuật âm nhạc truyền thống của người Nam Bộ, bắt nguồn từ nhạc lễ và nhạc sân khấu cải lương thế kỷ XIX. UNESCO công nhận Di sản văn hóa phi vật thể đại diện nhân loại năm 2013.',
    desc: 'Đờn ca tài tử is a traditional musical art of southern Vietnam, originating from ritual music and cải lương theatre of the 19th century. Inscribed on the UNESCO Representative List in 2013.',
  },
  {
    id: 5,
    name: 'Hát Xoan Phú Thọ',
    english: 'Xoan Singing of Phú Thọ',
    lat: 21.4092, lng: 105.4012,
    location: 'Phú Thọ · Đền Hùng',
    provinces: ['Phú Thọ'],
    year: '2017',
    status: 'inscribed',
    genre: 'singings',
    badge: 'UNESCO',
    desc_vi: 'Hát Xoan (hát Cửa đình) là loại hình nghệ thuật diễn xướng nghi lễ cổ của vùng đất tổ Hùng Vương, gắn với thờ cúng các vua Hùng. UNESCO ghi danh khẩn cấp năm 2011, chuyển sang Danh sách đại diện năm 2017.',
    desc: 'Xoan singing is a ritual performance art from the Hùng Kings\' ancestral land, associated with worship at the Hùng temples. UNESCO inscribed it on the Urgent Safeguarding List in 2011 and moved it to the Representative List in 2017.',
  },
  {
    id: 6,
    name: 'Dân ca Ví, Giặm Nghệ Tĩnh',
    english: 'Ví & Giặm Folk Songs of Nghệ Tĩnh',
    lat: 18.6796, lng: 105.6927,
    location: 'Nghệ An · Hà Tĩnh · Vùng Nghệ Tĩnh',
    provinces: ['Nghệ An','Hà Tĩnh'],
    year: '2014',
    status: 'inscribed',
    genre: 'singings',
    badge: 'UNESCO',
    desc_vi: 'Ví và Giặm là hai thể loại dân ca đặc trưng của người dân xứ Nghệ, được sử dụng trong lao động, sinh hoạt và bộc lộ tình cảm. UNESCO công nhận Di sản văn hóa phi vật thể đại diện năm 2014.',
    desc: 'Ví and Giặm are two distinctive folk song genres of the Nghệ Tĩnh region, performed during labour and daily life to express emotion and community bonds. Inscribed on the UNESCO Representative List in 2014.',
  },
  {
    id: 7,
    name: 'Tín ngưỡng thờ cúng Hùng Vương',
    english: 'Worship of the Hùng Kings in Phú Thọ',
    lat: 21.3254, lng: 105.2116,
    location: 'Phú Thọ · Đền Hùng',
    provinces: ['Phú Thọ'],
    year: '2012',
    status: 'inscribed',
    genre: 'belief',
    badge: 'UNESCO',
    desc_vi: 'Tín ngưỡng thờ cúng Hùng Vương là tục thờ tổ tiên sâu sắc nhất của người Việt, gắn với tín niệm các vua Hùng sáng lập nước. UNESCO công nhận Di sản văn hóa phi vật thể đại diện của nhân loại năm 2012.',
    desc: 'The worship of the Hùng Kings is the most profound ancestor-veneration practice of the Vietnamese, rooted in the legend of the Hùng Kings who founded the nation. Inscribed on the UNESCO Representative List in 2012.',
  },
  {
    id: 8,
    name: 'Hội Gióng Phù Đổng',
    english: 'Gióng Festival of Phù Đổng & Sóc Sơn',
    lat: 21.2766, lng: 105.8461,
    location: 'Hà Nội · Gia Lâm · Sóc Sơn',
    provinces: ['Hà Nội'],
    year: '2010',
    status: 'inscribed',
    genre: 'festival',
    badge: 'UNESCO',
    desc_vi: 'Hội Gióng là lễ hội lớn tưởng nhớ Thánh Gióng đánh thắng giặc Ân, truyền thuyết về anh hùng dân tộc. Được UNESCO công nhận Di sản văn hóa phi vật thể đại diện của nhân loại năm 2010.',
    desc: 'The Gióng Festival commemorates Saint Gióng, who defeated the Ân invaders according to Vietnamese legend. Inscribed on the UNESCO Representative List in 2010.',
  },
  {
    id: 9,
    name: 'Không gian văn hóa Cồng Chiêng Tây Nguyên',
    english: 'Gong Culture of the Central Highlands',
    lat: 12.7149, lng: 108.2436,
    location: 'Đắk Lắk · Gia Lai · Kon Tum',
    provinces: ['Đắk Lắk','Gia Lai','Kon Tum','Đắk Nông','Lâm Đồng'],
    year: '2008',
    status: 'inscribed',
    genre: 'instrumental',
    badge: 'UNESCO',
    desc_vi: 'Không gian văn hóa Cồng Chiêng Tây Nguyên gắn liền với đời sống tinh thần của các dân tộc Ba Na, Xê Đăng, Cơ Ho, M\'Nông, Ê Đê. UNESCO công nhận Di sản văn hóa phi vật thể đại diện của nhân loại năm 2008.',
    desc: 'The Gong Culture of the Central Highlands is central to the spiritual life of the Ba Na, Xê Đăng, Cơ Ho, M\'Nông and Ê Đê peoples. Inscribed on the UNESCO Representative List in 2008.',
  },
  {
    id: 10,
    name: 'Tín ngưỡng thờ Mẫu tam tòa',
    english: 'Viet Belief in Mother Goddesses of Three Realms',
    lat: 20.4195, lng: 106.1667,
    location: 'Nam Định · Đền Bà Chúa Xứ',
    provinces: ['Nam Định'],
    year: '2016',
    status: 'inscribed',
    genre: 'belief',
    badge: 'UNESCO',
    desc_vi: 'Tín ngưỡng thờ Mẫu tam tòa (Thiên – Địa – Thủy) thể hiện qua nghi lễ Hầu đồng và hát văn. UNESCO công nhận Di sản văn hóa phi vật thể đại diện của nhân loại năm 2016.',
    desc: 'The Vietnamese belief in the Mother Goddesses of the Three Realms (Heaven–Earth–Water) is expressed through Hầu đồng (spirit mediumship) rites and hát văn. Inscribed on the UNESCO Representative List in 2016.',
  },
  {
    id: 11,
    name: 'Nghệ thuật Bài Chòi',
    english: 'Bài Chòi Art of Central Vietnam',
    lat: 15.8801, lng: 108.3380,
    location: 'Quảng Nam · Quảng Ngãi · Bình Định',
    provinces: ['Quảng Nam','Quảng Ngãi','Bình Định','Phú Yên','Khánh Hòa'],
    year: '2017',
    status: 'inscribed',
    genre: 'singings',
    badge: 'UNESCO',
    desc_vi: 'Bài Chòi là nghệ thuật diễn xướng kết hợp giữa trò chơi bài và hát Wooden của nông dân miền Trung. UNESCO công nhận Di sản văn hóa phi vật thể đại diện của nhân loại năm 2017.',
    desc: 'Bài Chòi is a performative art combining card play with traditional singing by farmers of central Vietnam. Inscribed on the UNESCO Representative List in 2017.',
  },
  {
    id: 12,
    name: 'Hát Then người Tày, Nùng',
    english: 'Then Singing of the Tày & Nùng',
    lat: 22.6607, lng: 106.2520,
    location: 'Cao Bằng · Hà Giang · Lạng Sơn',
    provinces: ['Cao Bằng','Hà Giang','Lạng Sơn','Tuyên Quang','Thái Nguyên','Bắc Kạn'],
    year: '2019',
    status: 'national',
    genre: 'singings',
    badge: 'Quốc gia',
    desc_vi: 'Hát Then là thể loại dân ca nghi lễ của người Tây, Nùng, Thái ở vùng Đông Bắc, gắn liền với đàn tính. Được đưa vào Danh mục di sản văn hóa phi vật thể quốc gia và đang đề cử UNESCO.',
    desc: 'Then singing is a ritual folk music genre of the Tày, Nùng and Thái peoples of the northeast, accompanied by the tính lute. Listed as Vietnamese national intangible heritage; under UNESCO tentative nomination.',
  },
];

/* ═══════════════════════════════════════
   UNESCO STATUS CONFIGURATION (bilingual)
═══════════════════════════════════════ */
const STATUS_CONFIG = {
  urgent: {
    color:'#d4524a',
    vi: { label:'Danh sách cần bảo vệ khẩn cấp', short:'Cấp thiết' },
    en: { label:'Urgent Safeguarding List',    short:'Urgent' },
  },
  inscribed: {
    color:'#c9a84c',
    vi: { label:'Danh sách đại diện của nhân loại', short:'Đại diện' },
    en: { label:'Representative List of Humanity',  short:'Representative' },
  },
  national: {
    color:'#5a8a9f',
    vi: { label:'Di sản văn hóa phi vật thể quốc gia', short:'Quốc gia' },
    en: { label:'National Intangible Heritage',       short:'National' },
  },
  tentative: {
    color:'#8a7c5e',
    vi: { label:'Đề cử UNESCO',     short:'Đề cử' },
    en: { label:'Tentative UNESCO List', short:'Tentative' },
  },
};

/* — manual status overrides for entries whose status is ambiguous — */
const STATUS_OVERRIDES = {
  5: 'inscribed',  // Hát Xoan — moved from Urgent (2011) to Representative (2017)
};

/* ── STATUS reader — status is a direct field on each heritage item ── */
function getStatus(item) {
  if (item && STATUS_OVERRIDES[item.id]) return STATUS_OVERRIDES[item.id];
  return item.status || 'national';
}

/* ═══════════════════════════════════════
   HERITAGE GENRE CONFIGURATION (bilingual)
═══════════════════════════════════════ */
const GENRE_CONFIG = {
  instrumental: {
    color:'#4caf84',
    vi: { label:'Âm nhạc · Nhạc cụ', short:'Âm nhạc' },
    en: { label:'Instrumental Music', short:'Instrumental' },
  },
  singings: {
    color:'#c9943a',
    vi: { label:'Hát · Dân ca',        short:'Hát' },
    en: { label:'Singing · Folk Songs', short:'Singings' },
  },
  belief: {
    color:'#9b6fbf',
    vi: { label:'Tín ngưỡng · Lễ nghi', short:'Tín ngưỡng' },
    en: { label:'Belief & Ritual',      short:'Belief' },
  },
  festival: {
    color:'#c45c4a',
    vi: { label:'Lễ hội dân gian', short:'Lễ hội' },
    en: { label:'Folk Festival',  short:'Festival' },
  },
};

/* ── GENRE reader — genre is a direct field on each heritage item ── */
function getGenre(item) {
  return item.genre || '';
}