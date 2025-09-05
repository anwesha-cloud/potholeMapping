import json
from src.potholes.contracts import PotholeProps, to_feature, to_feature_collection, save_geojson

# Step A: Make one pothole object
p1 = PotholeProps(
    id=1,
    latitude=19.0760,
    longitude=72.8777,
    severity="moderate",
    detection_timestamp="2025-08-20T10:15:00Z",
    street_name="Dr Annie Besant Rd",
    street_direction="N",
    image_url="https://example.com/gsv/1"
)

# Step B: Convert to FeatureCollection
fc = to_feature_collection([to_feature(p1)])

# Step C: Save as GeoJSON
save_geojson(fc, "outputs/geojson/test_pothole.geojson")

print("✅ GeoJSON written successfully!")
print(json.dumps(fc, indent=2))
