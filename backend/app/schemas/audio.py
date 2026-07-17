from typing import List, Dict, Optional, Literal
from pydantic import BaseModel, Field


class GenreScore(BaseModel):
    label: Literal[
        "quan_ho", "ca_tru", "nha_nhac", "don_ca_tai_tu", "ho"
    ]
    confidence: float = Field(..., ge=0.0, le=1.0)
    all_scores: Dict[str, float] = Field(default_factory=dict)


class InstrumentScore(BaseModel):
    detected: List[Literal[
        "dan_bau", "dan_tranh", "dan_nhi", "dan_ty_ba", "sao",
        "ken", "tieu", "phach", "trong_de", "trong_chat", "mo", "voice"
    ]] = []
    all_scores: Dict[str, float] = Field(default_factory=dict)


class OrnamentEvent(BaseModel):
    time_seconds: float = Field(..., ge=0.0)
    technique: Literal[
        "nay_hat", "run_hat", "lay_hat", "so_hat", "nhap_hat",
        "chuyen_hat", "vuot_hat", "dam_hat", "roi_hat", "kep_hat"
    ]
    confidence: float = Field(..., ge=0.0, le=1.0)


class TechniqueScore(BaseModel):
    detected: List[Literal[
        "nay_hat", "run_hat", "lay_hat", "so_hat", "nhap_hat",
        "chuyen_hat", "vuot_hat", "dam_hat", "roi_hat", "kep_hat"
    ]] = []
    all_scores: Dict[str, float] = Field(default_factory=dict)
    ornament_timeline: List[OrnamentEvent] = []


class AudioAnalysisResponse(BaseModel):
    genre: GenreScore
    instruments: InstrumentScore
    techniques: TechniqueScore
    confidence: float = Field(..., ge=0.0, le=1.0)
    processing_time_ms: int = Field(..., ge=0)
    waveform_url: str