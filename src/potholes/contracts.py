from dataclasses import dataclass, asdict
from typing import Optional, Union, List, Dict, Any
import json

Severity = Union[int, str]  # 1..5 or "minor"|"moderate"|"severe"

@dataclass(frozen=True)
class PotholeProps:
    id: Union[str, int]
    latitude: float
    longitude: float
    severity: Severity
    detection_timestamp: str  # ISO 8601
    street_name: Optional[str] = None
    street_direction: Optional[str] = None
    image_url: Optional[str] = None

def to_feature(p: PotholeProps) -> Dict[str, Any]:
    return {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [p.longitude, p.latitude]},
        "properties": asdict(p),
    }

def to_feature_collection(features: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {"type": "FeatureCollection", "features": features}

def save_geojson(fc: Dict[str, Any], path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(fc, f, indent=2)
