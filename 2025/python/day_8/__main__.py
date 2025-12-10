from functools import reduce
import itertools
import math
from typing import NamedTuple

from common import get_input, timer


class Coordindate(NamedTuple):
    x: int
    y: int
    z: int

    def __str__(self) -> str:
        return f"(x={self.x},y={self.y},z={self.z})"

    def __repr__(self) -> str:
        return f"(x={self.x},y={self.y},z={self.z})"

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Coordindate):
            return self.x == value.x and self.y == value.y and self.z == value.z
        return False


def euclidean_distance(p: Coordindate, q: Coordindate) -> float:
    return math.sqrt(
        math.pow((p.x - q.x), 2) + math.pow((p.y - q.y), 2) + math.pow((p.z - q.z), 2)
    )


input = [
    Coordindate(*[int(s) for s in line.split(",")])
    for line in get_input().read_text().split("\n")
]

ds = []
for p, q in itertools.combinations(input, 2):
    ds.append((p, q, euclidean_distance(p, q)))
ds.sort(key=lambda x: x[2], reverse=True)


def part_1(ds):
    cs = []
    for _ in range(1000):
        jb = ds.pop()
        # potential circuit
        pc = {jb[0], jb[1]}
        nc = [c for c in cs if c & pc]
        cs = [c for c in cs if not c & pc]

        for c in nc:
            pc = pc | c

        cs.append(pc)

    scs = sorted([len(c) for c in cs], reverse=True)[:3]
    p1 = reduce(lambda x, y: x * y, scs, 1)

    print("part 1", p1)


with timer("part 1"):
    part_1(ds)
