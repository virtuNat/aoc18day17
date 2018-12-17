#!/usr/bin/env python
from sys import setrecursionlimit
from collections import defaultdict, Counter
# import pygame as pg
with open('Day17Input.txt', 'r') as ifile:
    iscan = [line.split(', ') for line in ifile]
    iscan = [[line[0][0], int(line[0][2:]), [int(c) for c in line[1][2:].split('..')]] for line in iscan]
gplot = defaultdict(lambda: '.')
for rcdir, v, (wmin, wmax) in iscan:
    for z in range(wmin, wmax+1):
        if rcdir == 'x':
            gplot[(v, z)] = '#'
        else:
            gplot[(z, v)] = '#'
xylst = list(zip(*gplot))
# xlmin, xlmax = min(xylst[0]), max(xylst[0])
ylmin, ylmax = min(xylst[1]), max(xylst[1])
# pg.init()
# clock = pg.time.Clock()
# pg.display.set_caption('Advent of Code Day 17 Simulator')
# screen = pg.display.set_mode((ylmax - ylmin + 101, xlmax - xlmin + 51))
# screen.fill((0, 0, 0))
# for x, y in gplot:
#     screen.set_at((y - ylmin + 50, x - xlmin + 25), 0x777777)

def water_fill(x, y):
    # for event in pg.event.get():
    #     if event.type == pg.QUIT:
    #         raise SystemExit
    if y > ylmax or gplot[(x, y)] in '#~|':
        return
    gplot[(x, y)] = '|'
    # screen.set_at((y - ylmin + 50, x - xlmin + 25), 0x00cccc)
    water_fill(x, y+1)
    if gplot[(x, y+1)] not in '#~':
        return
    xfmin = xfmax = None
    nx = x
    while True:
        nx -= 1
        if gplot[(nx, y)] in '#~':
            xfmin = nx + 1
            break
        gplot[(nx, y)] = '|'
        # screen.set_at((y - ylmin + 50, nx - xlmin + 25), 0x00cccc)
        water_fill(nx, y+1)
        if gplot[(nx, y+1)] not in '#~':
            break
        # pg.display.flip()
        # clock.tick(60)
    nx = x
    while True:
        nx += 1
        if gplot[(nx, y)] in '#~':
            xfmax = nx
            break
        gplot[(nx, y)] = '|'
        # screen.set_at((y - ylmin + 50, nx - xlmin + 25), 0x00cccc)
        water_fill(nx, y+1)
        if gplot[(nx, y+1)] not in '#~':
            break
        # pg.display.flip()
        # clock.tick(60)
    if xfmin is not None and xfmax is not None:
        for i in range(xfmin, xfmax):
            gplot[(i, y)] = '~'
            # screen.set_at((y - ylmin + 50, i - xlmin + 25), 0x0000cc)
    # pg.display.flip()
    # clock.tick(60)

setrecursionlimit(2000)
water_fill(500, 0)
wfcnt = Counter(v for k, v in gplot.items() if ylmin <= k[1] <= ylmax)
print(wfcnt['|'] + wfcnt['~'], wfcnt['~'])
# while True:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             raise SystemExit
