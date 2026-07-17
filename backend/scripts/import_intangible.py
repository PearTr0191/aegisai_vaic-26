"""
Import intangible heritage data into SQLite database.
Merges tangible artifacts with intangible heritage sites.
"""
import asyncio
import json
from datetime import datetime
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import async_session_maker, init_db
from app.models.site import HeritageSite, HeritageType, UNESCOStatus


INTANGIBLE_SITES = [
    {
        "id": "int-001",
        "name_vi": "Lễ hội Quan họ Bắc Ninh",
        "name_en": "Quan Ho Bac Ninh Festival",
        "description_vi": "Quan họ là dân ca đối đáp truyền thống của Bắc Ninh, hình thức biểu diễn chủ yếu là nam ca sĩ và nữ ca sĩ đối đáp nhau qua các câu hò.",
        "description_en": "Quan họ is a traditional folk singing style from Bắc Ninh province featuring call-and-response between male and female singers.",
        "latitude": 21.1861,
        "longitude": 106.0763,
        "province": "Bắc Ninh",
        "district": "Gây",
        "heritage_type": "intangible",
        "unesco_status": "inscribed",
        "cultural_layers": ["quan_ho", "bac_ninh", "folk_singing", "unesco"],
        "cover_image": "/images/quanho-cover.jpg",
        "audio_preview": "/audio/quanho-preview.mp3",
    },
    {
        "id": "int-002",
        "name_vi": "Nhà ca - Nơi lưu giữ di sản Ca trù",
        "name_en": "Traditional Ca tru House",
        "description_vi": "Ca trù là một loại hình nghệ thuật diễn xướng truyền thống của Việt Nam, kết hợp giữa ca nhảy và nhạc cụ đờn, nhị, sao.",
        "description_en": "Ca trù is a traditional Vietnamese form of chamber music performed with traditional instruments.",
        "latitude": 21.0285,
        "longitude": 105.8542,
        "province": "Hà Nội",
        "district": "Hoàn Kiếm",
        "heritage_type": "intangible",
        "unesco_status": "inscribed",
        "cultural_layers": ["ca_tru", "ha_noi", "chamber_music", "unesco"],
        "cover_image": "/images/catru-cover.jpg",
        "audio_preview": "/audio/catru-preview.mp3",
    },
    {
        "id": "int-003",
        "name_vi": "Nhã nhạc cung đình Huế",
        "name_en": "Hue Royal Court Music",
        "description_vi": "Nhã nhạc cung đình Huế là di sản tinh túy của triều đại nhà Nguyễn, biểu diễn sự uy nghi và thứ phái của hoàng gia.",
        "description_en": "The Hue Royal Court Music represents the musical traditions of the Nguyen Dynasty court.",
        "latitude": 16.4637,
        "longitude": 107.5909,
        "province": "Thừa Thiên Huế",
        "district": "Huế",
        "heritage_type": "intangible",
        "unesco_status": "inscribed",
        "cultural_layers": ["nha_nhac", "hue", "court_music", "unesco", "royal"],
        "cover_image": "/images/nhuanhac-cover.jpg",
        "audio_preview": "/audio/nhuanhac-preview.mp3",
    },
    {
        "id": "int-004",
        "name_vi": "Đờn ca tài tử Nam Bộ",
        "name_en": "Southern Don Ca Tai Tu Music",
        "description_vi": "Đờn ca tài tử là nghệ thuật âm nhạc truyền thống của miền Tây Nam Bộ, phản ánh đời sống và tâm tưởng của người dân cảnh.",
        "description_en": "Don ca tai tu is a traditional music form of southern Vietnam, combining vocal and instrumental performances.",
        "latitude": 10.0452,
        "longitude": 105.7469,
        "province": "Cần Thơ",
        "district": "Ninh Kiều",
        "heritage_type": "intangible",
        "unesco_status": "inscribed",
        "cultural_layers": ["don_ca_tai_tu", "mien_nam", "chamber_music", "unesco"],
        "cover_image": "/images/donantutu-cover.jpg",
        "audio_preview": "/audio/donantutu-preview.mp3",
    },
    {
        "id": "int-005",
        "name_vi": "Hò ca Nghệ An - Hò làng",
        "name_en": "Nghe An Work Songs (Hò)",
        "description_vi": "Hò làng là các điệu dân ca lao động truyền thống của người nông dân Nghệ An, được hát trong quá trình làm việc và vui chơi.",
        "description_en": "Traditional work songs from Nghệ An province, sung by farmers and laborers during harvests and fieldwork.",
        "latitude": 18.6796,
        "longitude": 105.6927,
        "province": "Nghệ An",
        "district": "Vinh",
        "heritage_type": "intangible",
        "unesco_status": "national",
        "cultural_layers": ["ho", "nghe_an", "work_songs", "labor", "national"],
        "cover_image": "/images/ho-nghean-cover.jpg",
        "audio_preview": "/audio/ho-nghean-preview.mp3",
    },
]


async def import_intangible_sites() -> int:
    """Import intangible heritage sites into database."""
    await init_db()
    
    async with async_session_maker() as db:
        count = 0
        for site in INTANGIBLE_SITES:
            stmt = insert(HeritageSite).values(
                id=site["id"],
                name_vi=site["name_vi"],
                name_en=site["name_en"],
                description_vi=site["description_vi"],
                description_en=site["description_en"],
                latitude=site["latitude"],
                longitude=site["longitude"],
                province=site["province"],
                district=site["district"],
                heritage_type=site["heritage_type"],
                unesco_status=site["unesco_status"],
                cultural_layers=site["cultural_layers"],
                cover_image=site["cover_image"],
                audio_preview=site["audio_preview"],
            )
            await db.execute(stmt)
            count += 1
        
        await db.commit()
        print(f"Imported {count} intangible heritage sites")
        return count


if __name__ == "__main__":
    asyncio.run(import_intangible_sites())