from common import get_input
import copy

grid = [[c for c in s] for s in get_input().read_text().split("\n")]

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


def remove_rolls(g):
    f = "."
    p = "@"
    r = []

    for y, row in enumerate(g):
        for x, col in enumerate(row):
            if col != f:
                a = 0
                for coord in coords:
                    yc, xc = y + coord[0], x + coord[1]
                    # check if coord is in bounds
                    if yc >= 0 and yc < len(g) and xc >= 0 and xc < len(row):
                        if g[yc][xc] == p:
                            a += 1

                if a < 4:
                    r.append((y, x))

    for c in r:
        g[c[0]][c[1]] = f

    return (g, r)


def part_1(g):
    g = copy.deepcopy(g)
    _, r = remove_rolls(g)

    print("part_1", len(r))


part_1(grid)


def part_2(g):
    g = copy.deepcopy(g)

    s = 0

    while True:
        g, r = remove_rolls(g.copy())
        print("removed", len(r), "rolls")
        if len(r) == 0:
            break
        else:
            s += len(r)

    print("part_2", s)


part_2(grid)
