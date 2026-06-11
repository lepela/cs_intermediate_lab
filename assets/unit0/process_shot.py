#!/usr/bin/env python3
"""u0 스크린샷 후처리: 브라우저 크롬(녹색 테마)+자동화 배너/글로우 자동 크롭 + 마커."""
import sys, numpy as np
from PIL import Image, ImageDraw

SHOTS = "/sessions/amazing-hopeful-dijkstra/mnt/PBL/tools/capture-watcher/_capture/shots"
ASSETS = "/sessions/amazing-hopeful-dijkstra/mnt/PBL/cs_intermediate_lab/assets/unit0"
M = 16  # 자동화 글로우 제거용 인셋

def detect_top(im):
    a = np.asarray(im.convert("RGB"))
    last_green = 0
    for y in range(0, min(260, a.shape[0])):
        r, g, b = a[y,:,0].mean(), a[y,:,1].mean(), a[y,:,2].mean()
        if g > r + 5 and g > b + 5:
            last_green = y
    return last_green + 4

def main():
    raw, out = sys.argv[1], sys.argv[2]
    im = Image.open(f"{SHOTS}/{raw}").convert("RGB")
    w, h = im.size
    top = detect_top(im) + M
    left, right, bottom = M, w - M, h - M
    crop = im.crop((left, top, right, bottom))
    cw, ch = crop.size
    if len(sys.argv) >= 5:
        mx, my = float(sys.argv[3]), float(sys.argv[4])
        mw = float(sys.argv[5]) if len(sys.argv) >= 7 else 1568.0
        mh = float(sys.argv[6]) if len(sys.argv) >= 7 else 699.0
        cx, cy = mx / mw * cw, my / mh * ch
        d = ImageDraw.Draw(crop)
        rds = 24
        for off in range(4):
            d.ellipse([cx-rds-off, cy-rds-off, cx+rds+off, cy+rds+off], outline=(255,120,0))
    crop.save(f"{ASSETS}/{out}.png")
    print(f"{out}.png saved: crop top={top} size={crop.size}")

main()
