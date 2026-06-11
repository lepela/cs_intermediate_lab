#!/usr/bin/env python3
"""핵심영역 타이트 크롭 + 콘텐츠 인식 글로우/테두리 트림 (블라인드 인셋 없음).
사용: python3 crop_region.py <raw.png> <out_name> <x0> <y0|auto> <x1> <y1>
 - 좌표는 RAW(원본 풀창) 픽셀 기준. y0=auto면 녹색 크롬 끝(콘텐츠 top) 자동 검출.
 - 크롭 후 각 변에서 '주황 글로우' 또는 '검은 창 테두리' 픽셀만 정확히 트림.
"""
import sys, numpy as np
from PIL import Image

SHOTS = "/sessions/confident-brave-dijkstra/mnt/PBL/tools/capture-watcher/_capture/shots"
ASSETS = "/sessions/confident-brave-dijkstra/mnt/PBL/cs_intermediate_lab/assets/unit0"

def detect_top(im):
    a = np.asarray(im.convert("RGB"))
    last = 0
    for y in range(0, min(260, a.shape[0])):
        r, g, b = a[y,:,0].mean(), a[y,:,1].mean(), a[y,:,2].mean()
        if g > r + 5 and g > b + 5:
            last = y
    return last + 2

def bad_line(line):
    # line: Nx3 array. True면 글로우(주황) 또는 검은테두리가 우세 → 트림 대상
    r, g, b = line[:,0].astype(int), line[:,1].astype(int), line[:,2].astype(int)
    orange = ((r > g + 6) & (r > b + 10)).mean()
    dark = ((r < 60) & (g < 60) & (b < 60)).mean()
    return (orange + dark) > 0.30

def trim(arr):
    t, b, l, r = 0, arr.shape[0], 0, arr.shape[1]
    while t < b and bad_line(arr[t, l:r]): t += 1
    while b > t and bad_line(arr[b-1, l:r]): b -= 1
    while l < r and bad_line(arr[t:b, l]): l += 1
    while r > l and bad_line(arr[t:b, r-1]): r -= 1
    return t, b, l, r

def main():
    raw, out, sx0, sy0, sx1, sy1 = sys.argv[1:7]
    im = Image.open(f"{SHOTS}/{raw}").convert("RGB")
    y0 = detect_top(im) if sy0 == "auto" else int(sy0)
    box = (int(sx0), y0, int(sx1), int(sy1))
    crop = im.crop(box)
    a = np.asarray(crop)
    t, b, l, r = trim(a)
    crop = crop.crop((l, t, r, b))
    crop.save(f"{ASSETS}/{out}.png")
    print(f"{out}.png box={box} -> trimmed size={crop.size}")

main()
