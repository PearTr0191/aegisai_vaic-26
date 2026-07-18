#!/usr/bin/env python3
"""Force-merge all adjacent polygons within each MultiPolygon feature."""
import json
from shapely.geometry import shape, mapping, Polygon, MultiPolygon
from shapely.ops import unary_union

INPUT  = "Project/vn_geo.json"
OUTPUT = "Project/vn_geo.json"

with open(INPUT, "r", encoding="utf-8") as f:
    geo = json.load(f)

final_features = []
for feat in geo["features"]:
    geom = feat["geometry"]
    name = feat["properties"]["name"]
    
    if geom["type"] != "MultiPolygon":
        final_features.append(feat)
        continue
    
    coords = geom["coordinates"]
    if len(coords) <= 1:
        final_features.append(feat)
        continue
    
    # Build individual polygons
    polys = []
    for ring in coords:
        try:
            p = Polygon(ring[0], ring[1:] if len(ring) > 1 else None)
            if not p.is_valid:
                p = p.buffer(0)
            polys.append(p)
        except Exception as e:
            print(f"  {name}: skip poly: {e}")
    
    if len(polys) <= 1:
        final_features.append(feat)
        continue
    
    before = len(polys)
    
    # Strategy: buffer out slightly, union, buffer back
    # This merges polygons that share edges or are very close
    try:
        buffered = [p.buffer(0.005) for p in polys]
        merged = unary_union(buffered)
        # Shrink back
        merged = merged.buffer(-0.005)
        
        if merged.is_valid and not merged.is_empty:
            if merged.geom_type == "Polygon":
                after = 1
            elif merged.geom_type == "MultiPolygon":
                after = len(merged.geoms)
            else:
                after = 1
            
            if after < before:
                print(f"  {name}: {before} -> {after}")
                final_features.append({
                    "type": "Feature",
                    "properties": feat["properties"],
                    "geometry": mapping(merged),
                })
                continue
    except Exception as e:
        print(f"  {name}: buffer merge failed: {e}")
    
    # Fallback: try direct union
    try:
        merged = unary_union(polys)
        if merged.is_valid and not merged.is_empty:
            if merged.geom_type == "Polygon":
                after = 1
            elif merged.geom_type == "MultiPolygon":
                after = len(merged.geoms)
            else:
                after = 1
            
            if after < before:
                print(f"  {name}: {before} -> {after} (direct)")
                final_features.append({
                    "type": "Feature",
                    "properties": feat["properties"],
                    "geometry": mapping(merged),
                })
                continue
    except Exception as e:
        print(f"  {name}: direct union failed: {e}")
    
    final_features.append(feat)

result = {"type": "FeatureCollection", "features": final_features}
with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, separators=(",", ":"))

print(f"Done: {len(final_features)} features")