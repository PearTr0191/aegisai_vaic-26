const TREASURES = [
  // ── BATCH 1 · Quyết định 1426/QĐ-TTg · 1/10/2012 ──────────────
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
    desc_vi: 'Hát Then là thể loại dân ca nghi lễ của người Tày, Nùng, Thái ở vùng Đông Bắc, gắn liền với đàn tính. Được đưa vào Danh mục di sản văn hóa phi vật thể quốc gia và đang đề cử UNESCO.',
    desc: 'Then singing is a ritual folk music genre of the Tày, Nùng and Thái peoples of the northeast, accompanied by the tính lute. Listed as Vietnamese national intangible heritage; under UNESCO tentative nomination.',
  },
];

/* ═══════════════════════════════════════
   LANGUAGE / I18N
═══════════════════════════════════════ */
let lang = localStorage.getItem('vnmt_lang') || 'vi';

const STRINGS = {
  vi: {
    headerEyebrow: 'Hiện Vật Được Công Nhận',
    titleLine1: 'Bảo Vật',
    titleEm: 'Quốc Gia',
    titleLine2: 'Việt Nam',
    statShownLabel: 'Hiển thị',
    statTotalLabel: 'Tổng số',
    statLocsLabel: 'Địa điểm',
    searchPlaceholder: 'Tìm theo tên hoặc địa điểm…',
    allEras: 'Tất cả thời kỳ',
    allTypes: 'Tất cả loại hình',
    mapReset: '⟳ Đặt lại',
    homeLink: '← Trang chủ',
    dbLink: 'Kho lưu trữ',
    viewToggleLabel: 'Xem theo',
    viewEra: 'Thời kỳ',
    viewType: 'Phân loại',
    tileStyleLabel: 'Kiểu bản đồ',
    tileOsm: 'Bản đồ đường phố',
    footerCopyright: '© 2026 Bảo vật Quốc gia Việt Nam',
    footerCredit: 'Bản đồ: <em>CartoDB / OpenStreetMap</em> · Phân cụm: <em>Leaflet.MarkerCluster</em>',
    legendEra: 'Thời kỳ',
    legendType: 'Phân loại',
  },
  en: {
    headerEyebrow: 'Nationally Recognized Artifacts',
    titleLine1: "Vietnam's",
    titleEm: 'National',
    titleLine2: 'Treasures',
    statShownLabel: 'Shown',
    statTotalLabel: 'Total',
    statLocsLabel: 'Locations',
    searchPlaceholder: 'Search by name or location…',
    allEras: 'All Eras',
    allTypes: 'All Types',
    mapReset: '⟳ Reset view',
    homeLink: '← Home',
    dbLink: 'Database',
    viewToggleLabel: 'View by',
    viewEra: 'Era',
    viewType: 'Category',
    tileStyleLabel: 'Map Style',
    tileOsm: 'Street Map',
    footerCopyright: '© 2026 Vietnam National Treasures',
    footerCredit: 'Map: <em>CartoDB / OpenStreetMap</em> · Clustering: <em>Leaflet.MarkerCluster</em>',
    legendEra: 'Era',
    legendType: 'Category',
  },
};

function t(key) { return STRINGS[lang][key]; }

function resultCountText(shown, total) {
  return lang === 'vi' ? `${shown} trên ${total} hiện vật` : `${shown} of ${total} artifacts`;
}
function clusterHoverText(n) {
  return lang === 'vi' ? `${n} hiện vật trong cụm này` : `${n} artifacts in this cluster`;
}

/* ═══════════════════════════════════════
   ERA & TYPE CONFIGURATION  (bilingual)
═══════════════════════════════════════ */
const ERA_CONFIG = {
  prehistoric: {
    color:'#c9943a',
    vi: { label:'Tiền sử · Sơ sử',  short:'Tiền sử' },
    en: { label:'Prehistoric · Protohistoric', short:'Prehistoric' },
  },
  century_1_10: {
    color:'#c47c5a',
    vi: { label:'Thế kỷ I – X',  short:'TK I–X' },
    en: { label:'1st–10th Century', short:'1st–10th c.' },
  },
  century_10_20: {
    color:'#4caf84',
    vi: { label:'Thế kỷ X – XIX', short:'TK X–XIX' },
    en: { label:'10th–19th Century', short:'10th–19th c.' },
  },
  modern_1945: {
    color:'#5a8a9f',
    vi: { label:'1900 – Nay', short:'1900–Nay' },
    en: { label:'1900–Present', short:'1900–Now' },
  },
};

const TYPE_CONFIG = {
  tools: {
    color:'#d4524a',
    vi: { label:'Công cụ & Vũ khí', short:'Công cụ' },
    en: { label:'Tools & Weapons', short:'Tools' },
  },
  religious: {
    color:'#9b7bdf',
    vi: { label:'Tôn giáo', short:'Tôn giáo' },
    en: { label:'Religious', short:'Religious' },
  },
  art: {
    color:'#e8a83c',
    vi: { label:'Nghệ thuật & Trang trí', short:'Nghệ thuật' },
    en: { label:'Art & Decoration', short:'Art' },
  },
  academic: {
    color:'#4a9e8a',
    vi: { label:'Học thuật & Văn bản', short:'Học thuật' },
    en: { label:'Academic & Documents', short:'Academic' },
  },
  craft: {
    color:'#e88d4a',
    vi: { label:'Nghề thủ công truyền thống', short:'Thủ công' },
    en: { label:'Traditional Craft', short:'Craft' },
  },
};

/* bilingual label readers — form is 'label' or 'short' */
function eraLabel(key, form='label')  { return ERA_CONFIG[key]?.[lang]?.[form]  || ''; }
function typeLabel(key, form='label') { return TYPE_CONFIG[key]?.[lang]?.[form] || ''; }

/* — manual status overrides for entries whose status is ambiguous — */
const STATUS_OVERRIDES = {
  5: 'inscribed',  // Hát Xoan — moved from Urgent (2011) to Representative (2017)
};

/* — manual type overrides for items that keyword-matching can't handle — */
/* ── TYPE reader — type is now a direct field on each artifact ── */
function getType(t) {
  return t.type || 'religious';
}


function getEra(t) {
  const id   = (t && t.id   !== undefined) ? t.id   : null;
  const year = (t && t.year !== undefined) ? t.year : String(t);

  if (id !== null && ERA_OVERRIDES[id]) return ERA_OVERRIDES[id];

  const y = String(year || '');
  if (['Đông Sơn','Phùng Nguyên','Đồng Nai'].some(k => y.includes(k))) return 'prehistoric';
  if (['Óc Eo','Chăm Pa'].some(k => y.includes(k)))                     return 'century_1_10';
  if (/20th|19\d{2}/.test(y))                                            return 'modern_1945';

  const yr = parseInt((y.match(/\d{3,4}/) || [])[0]);
  if (!isNaN(yr)) {
    if (yr >= 1900) return 'modern_1945';
    if (yr < 939)   return 'century_1_10';   // pre-independence Vietnam
  }
  return 'century_10_20';
}

/* ── Convenience wrappers: colour lookups ── */
function eraColor(t)  { return ERA_CONFIG[getEra(t)]?.color  || '#8a7c5e'; }
function typeColor(t) { return TYPE_CONFIG[getType(t)]?.color || '#8a7c5e'; }
function activeColor(t) { return viewMode === 'era' ? eraColor(t) : typeColor(t); }

/* ═══════════════════════════════════════
   STATE
═══════════════════════════════════════ */
let viewMode     = 'era';   // 'era' | 'type'
let activeFilter = 'all';   // era key, type key, or 'all'
let searchQuery  = '';
let activeItemId = null;

/* ═══════════════════════════════════════
   MAP INIT
═══════════════════════════════════════ */
const map = L.map('map', {
  center:[16.0, 107.8], zoom:5.4, zoomControl:false, preferCanvas:true
});
/* Zoom control removed — scroll-wheel zoom, double-click zoom, and
   click-to-zoom on clusters remain fully functional without it.
   This also frees up the bottom-right corner for the Map Style box. */

const TILES = {
  positron:{ url:'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
             opt:{ attribution:'&copy; OpenStreetMap contributors &copy; CARTO',
                   subdomains:'abcd', maxZoom:19 }},
  osm:     { url:'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
             opt:{ attribution:'&copy; OpenStreetMap contributors', maxZoom:19 }},
};
let currentTile = L.tileLayer(TILES.positron.url, TILES.positron.opt).addTo(map);

document.querySelectorAll('.tile-option').forEach(btn => {
  btn.addEventListener('click', () => {
    const k = btn.dataset.tile;
    if (!TILES[k]) return;
    map.removeLayer(currentTile);
    currentTile = L.tileLayer(TILES[k].url, TILES[k].opt).addTo(map);
    currentTile.bringToBack();
    document.querySelectorAll('.tile-option').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  });
});

/* ═══════════════════════════════════════
   CLUSTER PIE CHART ICON
═══════════════════════════════════════ */
function clusterIcon(cluster) {
  const n  = cluster.getChildCount();
  const sz = n < 5 ? 38 : n < 10 ? 50 : n < 20 ? 62 : 76;
  const cx = sz / 2;
  const r  = cx - 3;
  const ir = cx * 0.38;
  const fs = n >= 100 ? 11 : n >= 10 ? 13 : 14;

  const CONFIG = viewMode === 'era' ? ERA_CONFIG : TYPE_CONFIG;

  /* tally the active dimension from each child marker */
  const counts = {};
  cluster.getAllChildMarkers().forEach(m => {
    const key = viewMode === 'era' ? (m._era || 'century_10_20')
                                   : (m._type || 'religious');
    counts[key] = (counts[key] || 0) + 1;
  });

  const slices = Object.entries(counts).sort((a, b) => b[1] - a[1]);

  /* SVG pie slices */
  let paths    = '';
  let dividers = '';
  let angle    = -90;

  for (const [key, count] of slices) {
    const color    = CONFIG[key]?.color || '#8a7c5e';
    const sweepDeg = (count / n) * 360;

    if (sweepDeg >= 359.9) {
      paths = `<circle cx="${cx}" cy="${cx}" r="${r}" fill="${color}"/>`;
      break;
    }
    const a1 = angle * Math.PI / 180;
    const a2 = (angle + sweepDeg) * Math.PI / 180;
    const x1 = (cx + r * Math.cos(a1)).toFixed(2);
    const y1 = (cx + r * Math.sin(a1)).toFixed(2);
    const x2 = (cx + r * Math.cos(a2)).toFixed(2);
    const y2 = (cx + r * Math.sin(a2)).toFixed(2);

    paths    += `<path d="M${cx},${cx} L${x1},${y1} A${r},${r} 0 ${sweepDeg>180?1:0},1 ${x2},${y2} Z" fill="${color}"/>`;
    dividers += `<line x1="${cx}" y1="${cx}" x2="${x1}" y2="${y1}" stroke="white" stroke-width="1.5" stroke-linecap="round"/>`;
    angle    += sweepDeg;
  }
  return `<svg width="${sz}" height="${sz}" viewBox="0 0 ${sz} ${sz}" xmlns="http://www.w3.org/2000/svg">
    <circle cx="${cx}" cy="${cx}" r="${r+1}" fill="rgba(10,9,0,0.3)"/>
    ${paths}
    ${slices.length > 1 ? dividers : ''}
    <circle cx="${cx}" cy="${cx}" r="${ir}" fill="rgba(10,9,0,0.85)"/>
    <text x="${cx}" y="${cx}" text-anchor="middle" dominant-baseline="central"
          fill="#e8c96a" font-family="DM Sans,sans-serif" font-weight="700"
          font-size="18px">${total}</text>
  </svg>`;
}

/* Show province pie-chart modal — lists each heritage item with a
   clickable row that opens the full detail modal. */
function showProvinceModal(provinceName) {
  const artifacts = provinceIndex[provinceName] || [];
  const total = artifacts.length;
  const CONFIG = viewMode === 'status' ? STATUS_CONFIG : GENRE_CONFIG;

  const counts = {};
  artifacts.forEach(t => {
    const key = viewMode === 'status' ? getStatus(t) : getGenre(t);
    counts[key] = (counts[key] || 0) + 1;
  });

  const pieSVG = total > 0 ? buildProvincePieSVG(counts, total) : '';
  const legendRows = Object.entries(counts).sort((a,b) => b[1]-a[1]).map(([key, count]) => {
    const cfg = CONFIG[key];
    const label = viewMode === 'status' ? statusLabel(key, 'short') : genreLabel(key, 'short');
    return `<div class="province-pie-row">
      <span class="province-pie-dot" style="background:${cfg?.color || '#8a7c5e'}"></span>
      <span class="province-pie-label">${label}</span>
      <span class="province-pie-count">${count}</span>
    </div>`;
  }).join('');

  /* List of heritage items — clicking a row opens its detail modal. */
  const itemRows = artifacts.map(t => {
    const status = getStatus(t);
    const genre  = getGenre(t);
    const color  = activeColor(t);
    const title  = lang === 'vi' ? t.name : t.english;
    const sub    = lang === 'vi' ? t.english : t.name;
    return `
      <div class="province-item" data-id="${t.id}">
        <span class="province-item-dot" style="background:${color}"></span>
        <div class="province-item-body">
          <div class="province-item-title">${title}</div>
          <div class="province-item-sub">${sub}</div>
          <div class="province-item-tags">
            <span style="color:${statusColor(t)}">${statusLabel(status,'short')}</span>
            <span style="color:${genreColor(t)}">${genreLabel(genre,'short')}</span>
          </div>
        </div>
        <span class="province-item-cta">${t('pieCta')}</span>
      </div>`;
  }).join('');

  const dimLabel = viewMode === 'status'
    ? (lang === 'vi' ? 'Phân bố UNESCO' : 'UNESCO status distribution')
    : (lang === 'vi' ? 'Phân bố thể loại' : 'Genre distribution');

  const heritageLabel = lang === 'vi' ? 'Di sản trong tỉnh' : 'Heritage in this province';

  const html = total > 0 ? `
    <div class="province-modal-title">${provinceName}</div>
    <div class="province-modal-sub">${dimLabel}</div>
    <div class="province-pie-wrap">
      <div class="province-pie">${pieSVG}</div>
      <div class="province-pie-legend">${legendRows}</div>
    </div>
    <div class="province-pie-total">
      ${lang === 'vi' ? 'Tổng di sản' : 'Total heritage'}: <strong>${total}</strong>
    </div>
    <div class="province-item-list-label">${heritageLabel}</div>
    <div class="province-item-list">${itemRows}</div>
  ` : `
    <div class="province-modal-title">${provinceName}</div>
    <div class="province-modal-sub">${dimLabel}</div>
    <div class="province-pie-empty">
      ${lang === 'vi' ? 'Chưa có di sản phi vật thể trong tỉnh này' : 'No intangible heritage in this province'}
    </div>
  `;
}

/* rebuilds every marker's tooltip content to match the current language */
function refreshMarkerTooltips() {
  TREASURES.forEach(t => ITEM_MARKERS[t.id]?.setTooltipContent(buildTooltipHTML(t)));
}

/* builds the rich content shown inside the click-to-open detail modal */
function buildModalHTML(t) {
  const title = lang === 'vi' ? t.name : t.english;
  const engTitle = lang === 'vi' ? t.english : '';
  const era   = getEra(t);
  const type  = getType(t);
  const eraC  = ERA_CONFIG[era]?.color  || '#8a7c5e';
  const typeC = TYPE_CONFIG[type]?.color || '#8a7c5e';
  const desc  = lang === 'vi' ? (t.desc_vi || t.desc) : t.desc;
  const pending = (lang === 'vi' && !t.desc_vi)
    ? ' <span class="desc-pending">(EN)</span>' : '';
  const imageUrl = t.image || `images/artifacts/${t.id}.jpg`;

  return `
    <div class="modal-image-container">
      <img src="${imageUrl}" alt="${title}" class="modal-image" onerror="this.onerror=null; this.src='images/artifacts/placeholder.svg'" />
    </div>
    <div class="modal-badge-row">
      <span class="modal-badge" style="color:${eraC};border-color:${eraC}55">${eraLabel(era)}</span>
      <span class="modal-badge" style="color:${typeC};border-color:${typeC}55">${typeLabel(type)}</span>
      <span class="modal-badge modal-badge-badge" style="color:${eraC};border-color:${eraC}55">${t.badge || 'Artifact'}</span>
    </div>
    <div class="modal-title">${title}</div>
    ${engTitle ? `<div class="modal-subtitle">${engTitle}</div>` : ''}
    <div class="modal-info-grid">
      <div class="modal-info-item">
        <div class="modal-info-label">📅 Era/Year</div>
        <div class="modal-info-value">${t.year}</div>
      </div>
      <div class="modal-info-item">
        <div class="modal-info-label">🏷️ Category</div>
        <div class="modal-info-value">${typeLabel(type)}</div>
      </div>
      <div class="modal-info-item">
        <div class="modal-info-label">📍 Location</div>
        <div class="modal-info-value">${t.location}</div>
      </div>
      <div class="modal-info-item">
        <div class="modal-info-label">🗺️ Coordinates</div>
        <div class="modal-info-value">${t.lat.toFixed(4)}, ${t.lng.toFixed(4)}</div>
      </div>
    </div>
    <div class="modal-desc-section">
      <div class="modal-desc-label">Description</div>
      <div class="modal-desc">${desc}${pending}</div>
    </div>
  `;
}

function openArtifactModal(id) {
  const t = TREASURES.find(x => x.id === id);
  if (!t) return;
  document.getElementById('modal-content').innerHTML = buildModalHTML(t);
  document.getElementById('modal-overlay').classList.add('visible');
}

function closeArtifactModal() {
  document.getElementById('modal-overlay').classList.remove('visible');
  activeItemId = null;
  hideMapInfoBox();
  renderCards();
}

document.getElementById('modal-close').addEventListener('click', closeArtifactModal);
document.getElementById('modal-overlay').addEventListener('click', e => {
  if (e.target.id === 'modal-overlay') closeArtifactModal();
});
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeArtifactModal();
});

TREASURES.forEach(t => {
  const marker = L.marker([t.lat, t.lng], { icon: makeItemIcon(t) });
  marker._era  = getEra(t);
  marker._type = getType(t);

  /* hover → small tooltip above the dot (individual markers only, not clusters) */
  marker.bindTooltip(buildTooltipHTML(t), {
    direction:'top', offset:[0,-12], opacity:1, className:'artifact-tooltip'
  });

  /* click → flies to the dot and opens the full detail modal */
  marker.on('click', () => activateItem(t.id));
  ITEM_MARKERS[t.id] = marker;
});

/* ═══════════════════════════════════════
   FILTERING
═══════════════════════════════════════ */
function getFilteredItems() {
  let items = [...TREASURES];

  if (activeFilter !== 'all') {
    if (viewMode === 'era')
      items = items.filter(t => getEra(t)  === activeFilter);
    else
      items = items.filter(t => getType(t) === activeFilter);
  }
  if (searchQuery) {
    const q = searchQuery;
    items = items.filter(t =>
      t.name.toLowerCase().includes(q)     ||
      t.english.toLowerCase().includes(q)  ||
      t.location.toLowerCase().includes(q) ||
      t.year.toLowerCase().includes(q)
    );
  }
  return items;
}

/* ═══════════════════════════════════════
   MAP MARKERS — sorted so spider is ordered
═══════════════════════════════════════ */
function updateMapMarkers(items) {
  clusterGroup.clearLayers();

  const ORDER_ERA  = ['prehistoric','century_1_10','century_10_20','modern_1945'];
  const ORDER_TYPE = ['tools','religious','art','academic'];

  const sorted = [...items].sort((a, b) => {
    if (viewMode === 'era') {
      const d = ORDER_ERA.indexOf(getEra(a)) - ORDER_ERA.indexOf(getEra(b));
      return d !== 0 ? d : a.name.localeCompare(b.name);
    } else {
      const d = ORDER_TYPE.indexOf(getType(a)) - ORDER_TYPE.indexOf(getType(b));
      return d !== 0 ? d : a.name.localeCompare(b.name);
    }
  });

  sorted.forEach(t => clusterGroup.addLayer(ITEM_MARKERS[t.id]));
}

/* ═══════════════════════════════════════
   RENDER FILTER BAR  (dynamic)
═══════════════════════════════════════ */
function renderFilterBar() {
  const CONFIG   = viewMode === 'era' ? ERA_CONFIG : TYPE_CONFIG;
  const allLabel = viewMode === 'era' ? t('allEras') : t('allTypes');

  document.getElementById('filter-bar').innerHTML = `
    <button class="filter-btn ${activeFilter==='all'?'active':''}" data-filter="all">${allLabel}</button>
    ${Object.entries(CONFIG).map(([key, cfg]) => {
      const active = activeFilter === key;
      const short  = cfg[lang]?.short || '';
      return `<button class="filter-btn ${active?'active':''}" data-filter="${key}"
                style="${active?`border-color:${cfg.color};color:${cfg.color};background:${cfg.color}22`:''}">
        <span style="display:inline-block;width:7px;height:7px;border-radius:50%;
                     background:${cfg.color};margin-right:5px;vertical-align:middle;"></span>
        ${short}
      </button>`;
    }).join('')}
  `;

  document.querySelectorAll('#filter-bar .filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      activeFilter = btn.dataset.filter;
      activeItemId = null;
      renderFilterBar();
      renderCards();
    });
  });
}

/* ═══════════════════════════════════════
   RENDER MAP LEGEND  (dynamic)
═══════════════════════════════════════ */
function renderLegend() {
  const CONFIG = viewMode === 'era' ? ERA_CONFIG : TYPE_CONFIG;
  const title  = viewMode === 'era' ? t('legendEra') : t('legendType');
  document.getElementById('map-legend').innerHTML = `
    <div class="legend-title">${title}</div>
    ${Object.entries(CONFIG).map(([, cfg]) => `
      <div class="legend-row">
        <span class="legend-dot" style="background:${cfg.color}"></span>
        ${cfg[lang]?.short || ''}
      </div>`).join('')}
  `;
}

/* ═══════════════════════════════════════
   RENDER CARDS
═══════════════════════════════════════ */
function renderCards() {
  const items = getFilteredItems();

  document.getElementById('stat-shown').textContent = items.length;
  document.getElementById('stat-total').textContent = TREASURES.length;
  document.getElementById('stat-locs').textContent  =
    new Set(items.map(t => `${t.lat.toFixed(4)},${t.lng.toFixed(4)}`)).size;
  document.getElementById('result-count').textContent =
    resultCountText(items.length, TREASURES.length);

  updateMapMarkers(items);

  document.getElementById('artifact-list').innerHTML = items.map((t, i) => {
    const era   = getEra(t);
    const type  = getType(t);
    const color = activeColor(t);
    const badge = viewMode === 'era'
      ? eraLabel(era, 'short')
      : typeLabel(type, 'short');
    const title = lang === 'vi' ? t.name : t.english;
    return `
      <div class="a-card${activeItemId===t.id?' active':''}"
           data-id="${t.id}"
           onclick="activateItem(${t.id})"
           style="animation-delay:${Math.min(i*0.035,0.5)}s">
        <div class="a-num" style="color:${color}">${String(t.id).padStart(2,'0')}</div>
        <div class="a-body">
          <div class="a-title">${title}</div>
          <div class="a-desc">${lang === 'vi' ? (t.desc_vi || t.desc) : t.desc}${(lang === 'vi' && !t.desc_vi) ? ' <span class="desc-pending">(EN)</span>' : ''}</div>
          <div class="a-loc"><span class="a-pin">●</span>${t.location}</div>
        </div>
        <span class="a-badge" style="color:${color};border-color:${color}33">${badge}</span>
      </div>`;
  }).join('');
}

/* ═══════════════════════════════════════
   ACTIVATE ITEM
═══════════════════════════════════════ */
function activateItem(id) {
  activeItemId = id;
  const t = TREASURES.find(x => x.id === id);
  if (!t) return;

  renderActiveMapInfo();
  openArtifactModal(id);

  const targetZoom = Math.max(map.getZoom(), 14);
  map.flyTo([t.lat, t.lng], targetZoom, { duration:1.2, easeLinearity:0.25 });

  renderCards();
  setTimeout(() => {
    document.querySelector(`.a-card[data-id="${id}"]`)
      ?.scrollIntoView({ behavior:'smooth', block:'nearest' });
  }, 50);
}

/* ═══════════════════════════════════════
   VIEW TOGGLE  (Era ↔ Category)
═══════════════════════════════════════ */
document.querySelectorAll('.view-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    viewMode     = btn.dataset.view;
    activeFilter = 'all';
    activeItemId = null;
    document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    refreshMarkerIcons();
    renderFilterBar();
    renderLegend();
    clusterGroup.refreshClusters();
    renderCards();
  });
});

/* ═══════════════════════════════════════
   CLUSTER HOVER HINT
═══════════════════════════════════════ */
clusterGroup.on('clustermouseover', e => {
  showMapInfoBox(`
    <div class="map-info-count" id="map-info-count">${clusterHoverText(e.layer.getChildCount())}</div>
  `);
});
clusterGroup.on('clustermouseout', () => {
  renderActiveMapInfo();
});

/* ═══════════════════════════════════════
   SEARCH
═══════════════════════════════════════ */
document.getElementById('search-input').addEventListener('input', e => {
  searchQuery = e.target.value.toLowerCase().trim();
  renderCards();
});

/* ═══════════════════════════════════════
   RESET
═══════════════════════════════════════ */
document.getElementById('map-reset').addEventListener('click', () => {
  map.flyTo([16.0, 107.8], 5.4, { duration:1.0 });
  activeItemId = null;
  hideMapInfoBox();
  renderCards();
});

/* ═══════════════════════════════════════
   STATIC TEXT (non-data UI chrome)
═══════════════════════════════════════ */
function showMapInfoBox(html) {
  const box = document.getElementById('map-info');
  box.innerHTML = html;
  box.classList.add('visible');
}

function hideMapInfoBox() {
  document.getElementById('map-info').classList.remove('visible');
}

/* shows the currently selected artifact's info, or hides the box if none is selected */
function renderActiveMapInfo() {
  if (activeItemId === null) { hideMapInfoBox(); return; }
  const t = TREASURES.find(x => x.id === activeItemId);
  if (!t) { hideMapInfoBox(); return; }
  const title = lang === 'vi' ? t.name : t.english;
  showMapInfoBox(`
    <div class="map-info-title">${title}</div>
    <div class="map-info-sub">${t.location}</div>
    <div class="map-info-count" id="map-info-count"></div>
  `);
}

function applyStaticI18n() {
  document.documentElement.lang = lang;
  document.documentElement.classList.toggle('lang-vi', lang === 'vi');

  document.getElementById('header-eyebrow').textContent = t('headerEyebrow');
  document.getElementById('title-line1').textContent    = t('titleLine1');
  document.getElementById('title-em').textContent       = t('titleEm');
  document.getElementById('title-line2').textContent    = t('titleLine2');

  document.getElementById('stat-shown-label').textContent = t('statShownLabel');
  document.getElementById('stat-total-label').textContent = t('statTotalLabel');
  document.getElementById('stat-locs-label').textContent  = t('statLocsLabel');

  document.getElementById('search-input').placeholder = t('searchPlaceholder');

  document.getElementById('map-reset').textContent = t('mapReset');
  const hl = document.getElementById('lang-home-link');
  if (hl) hl.textContent = t('homeLink');
  const dl = document.getElementById('lang-db-link');
  if (dl) dl.textContent = t('dbLink');

  document.getElementById('view-toggle-label').textContent = t('viewToggleLabel');
  document.querySelector('.view-btn[data-view="era"]').textContent  = t('viewEra');
  document.querySelector('.view-btn[data-view="type"]').textContent = t('viewType');

  document.getElementById('tile-switcher-label').textContent = t('tileStyleLabel');
  document.getElementById('tile-osm-label').textContent      = t('tileOsm');

  document.getElementById('footer-copyright').textContent = t('footerCopyright');
  document.getElementById('footer-credit').innerHTML      = t('footerCredit');

  document.querySelectorAll('.lang-btn').forEach(b =>
    b.classList.toggle('active', b.dataset.lang === lang)
  );

  /* re-render whatever the map-info box should currently show, in the new language */
  renderActiveMapInfo();
}

/* ═══════════════════════════════════════
   LANGUAGE TOGGLE
═══════════════════════════════════════ */
document.querySelectorAll('.lang-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    if (btn.dataset.lang === lang) return;
    lang = btn.dataset.lang;
    localStorage.setItem('vnmt_lang', lang);

    applyStaticI18n();
    refreshMarkerTooltips();
    renderFilterBar();
    renderLegend();
    renderCards();
    if (document.getElementById('modal-overlay').classList.contains('visible')) {
      openArtifactModal(activeItemId);
    }
    setTimeout(() => map.invalidateSize(), 50);
  });
});

/* ═══════════════════════════════════════
   URL PARAMETER — era/type deep-link
   e.g. VNMT.html?era=prehistoric
        VNMT.html?type=religious
═══════════════════════════════════════ */
(function readURLParams() {
  const p = new URLSearchParams(window.location.search);
  const urlEra  = p.get('era');
  const urlType = p.get('type');
  if (urlEra && ERA_CONFIG[urlEra]) {
    viewMode     = 'era';
    activeFilter = urlEra;
    document.querySelector('.view-btn[data-view="era"]')?.classList.add('active');
    document.querySelector('.view-btn[data-view="type"]')?.classList.remove('active');
  } else if (urlType && TYPE_CONFIG[urlType]) {
    viewMode     = 'type';
    activeFilter = urlType;
    document.querySelector('.view-btn[data-view="era"]')?.classList.remove('active');
    document.querySelector('.view-btn[data-view="type"]')?.classList.add('active');
  }
})();

  /* ═══════════════════════════════════════
     INTANGIBLE HERITAGE INTEGRATION
   ═══════════════════════════════════════ */
  const INTANGIBLE_HERITAGE = [
    {
      id: "int-001",
      name: "Lễ hội Quan họ Bắc Ninh",
      english: "Quan Ho Bac Ninh Festival",
      location: "Bắc Ninh",
      lat: 21.1861, lng: 106.0763,
      category: "intangible",
      badge: "UNESCO",
      type: "folk_singing",
      year: "2009",
      desc: "Traditional folk singing with call-and-response between male and female singers.",
      desc_vi: "Quan họ là dân ca đối đáp truyền thống của Bắc Ninh.",
      audio_preview: "/audio/quanho-preview.mp3"
    },
    {
      id: "int-002",
      name: "Ca trù Hà Nội",
      english: "Traditional Ca tru Music",
      location: "Hà Nội",
      lat: 21.0285, lng: 105.8542,
      category: "intangible",
      badge: "UNESCO",
      type: "chamber_music",
      year: "2009",
      desc: "Vietnamese chamber music with traditional instruments.",
      desc_vi: "Ca trù là nghệ thuật diễn xướng truyền thống kết hợp ca nhảy và nhạc cụ.",
      audio_preview: "/audio/catru-preview.mp3"
    },
    {
      id: "int-003",
      name: "Nhã nhạc cung đình Huế",
      english: "Hue Royal Court Music",
      location: "Thừa Thiên Huế",
      lat: 16.4637, lng: 107.5909,
      category: "intangible",
      badge: "UNESCO",
      type: "court_music",
      year: "2003",
      desc: "Musical traditions of the Nguyen Dynasty court.",
      desc_vi: "Nhã nhạc cung đình Huế là di sản tinh túy của triều đại nhà Nguyễn.",
      audio_preview: "/audio/nhuanhac-preview.mp3"
    },
    {
      id: "int-004",
      name: "Đờn ca tài tử Nam Bộ",
      english: "Southern Don Ca Tai Tu Music",
      location: "Cần Thơ",
      lat: 10.0452, lng: 105.7469,
      category: "intangible",
      badge: "UNESCO",
      type: "chamber_music",
      year: "2014",
      desc: "Traditional music form of southern Vietnam.",
      desc_vi: "Đờn ca tài tử là nghệ thuật âm nhạc truyền thống miền Tây Nam Bộ.",
      audio_preview: "/audio/donantutu-preview.mp3"
    },
    {
      id: "int-005",
      name: "Hò ca Nghệ An",
      english: "Nghe An Work Songs",
      location: "Nghệ An",
      lat: 18.6796, lng: 105.6927,
      category: "intangible",
      badge: "National",
      type: "work_songs",
      year: "2015",
      desc: "Traditional work songs sung by farmers.",
      desc_vi: "Hò làng là dân ca lao động truyền thống của người nông dân.",
      audio_preview: "/audio/ho-nghean-preview.mp3"
    }
  ];

  // Merge tangible and intangible data
  const ALL_TREASURES = [...TREASURES, ...INTANGIBLE_HERITAGE];

  // Add intangible to type config for filtering
  const INTANGIBLE_TYPE_CONFIG = {
    ...TYPE_CONFIG,
    intangible: { label_vi: "Di sản vô hình", label_en: "Intangible Heritage", icon: "🎵" },
    folk_singing: { label_vi: "Hát dân ca", label_en: "Folk Singing", icon: "🎤" },
    chamber_music: { label_vi: "Nhạc cung đình", label_en: "Chamber Music", icon: "🎼" },
    court_music: { label_vi: "Nhạc triều đại", label_en: "Court Music", icon: "👑" },
    work_songs: { label_vi: "Hò ca", label_en: "Work Songs", icon: "🌾" }
  };

  /* ═══════════════════════════════════════
     CHAT API INTEGRATION
   ═══════════════════════════════════════ */
  async function callArtisanAPI(message, lang = "vi") {
    try {
      const resp = await fetch("/api/v1/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message, lang })
      });
      if (resp.ok) {
        const data = await resp.json();
        return data.response || "Xin lỗi, tôi chưa có câu trả lời.";
      }
    } catch (e) {
      console.error("Chat API error:", e);
    }
    return "Xin lỗi, dịch vụ đang tạm ngưng. Vui lòng thử lại sau.";
  }

  // Expose for global use
  window.INTANGIBLE_HERITAGE = INTANGIBLE_HERITAGE;
  window.ALL_TREASURES = ALL_TREASURES;
  window.callArtisanAPI = callArtisanAPI;

  /* ═══════════════════════════════════════
   INIT
   ═══════════════════════════════════════ */
  applyStaticI18n();
  renderFilterBar();
  renderLegend();
  renderCards();
  setTimeout(() => map.invalidateSize(), 50);
