from typing import Dict, List, Tuple
from common import get_input, timer
import copy

input = [[c for c in s] for s in get_input().read_text().split("\n")]

coords = [
    # cardinal
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
    # orthogonal
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]

# with timer("init"):
acc = []
wh = {}
for y, row in enumerate(input):
    for x, col in enumerate(row):
        if col == "@":
            # init to zero
            wh[(y, x)] = 0

# fill with N
for key in wh:
    a = 0
    for coord in coords:
        yc, xc = key[0] + coord[0], key[1] + coord[1]
        if (yc, xc) in wh:
            a += 1

    wh[key] = a
    if a < 4:
        acc.append(key)


def remove_rolls(wh, r) -> Tuple[Dict, List[Tuple[int, int]], int]:

    # find n < 4
    # find adjacent for each n < 4
    # only recalc adjacent

    for key in r:
        del wh[key]

    adj = []
    nacc = set()
    for key in r:
        for coord in coords:
            yc, xc = key[0] + coord[0], key[1] + coord[1]
            if (yc, xc) in wh:
                adj.append((yc, xc))

    for key in adj:
        a = 0
        for coord in coords:
            yc, xc = key[0] + coord[0], key[1] + coord[1]
            if (yc, xc) in wh:
                a += 1
        wh[key] = a
        if a < 4:
            nacc.add(key)

    rc = len(r)

    return (wh, list(nacc), rc)


def part_1(g, acc):
    g = copy.deepcopy(g)
    acc = acc.copy()

    _, acc, r = remove_rolls(g, acc)

    print("part_1", r)


with timer("part_1"):
    part_1(wh, acc)


def part_2(g, acc):

    g = copy.deepcopy(g)
    acc = acc.copy()
    s = 0
    while True:
        with timer("rr"):
            g, acc, r = remove_rolls(g, acc)
            if r == 0:
                break
            else:
                s += r

    print("part_2", s)


with timer("part_2"):
    part_2(wh, acc)
