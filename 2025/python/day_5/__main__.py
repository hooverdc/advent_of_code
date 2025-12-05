from typing import Tuple
from common import get_input, timer

# init

ing_ranges, ing_ids = get_input().read_text().split("\n\n")

ing_ranges = [
    tuple(int(s) for s in ing_range.split("-")) for ing_range in ing_ranges.split("\n")
]
ing_ids = [int(ing_id) for ing_id in ing_ids.split("\n")]

# part 1


def in_range(n: int, r: Tuple[int, int]) -> bool:
    return n >= r[0] and n <= r[1]


def part_1(irs, ids):
    s = 0

    for _id in ids:
        for ir in irs:
            if in_range(_id, ir):
                # print("ID ", ing_id, "is fresh")
                s += 1
                break

    print("part_1", s)


with timer("part_1"):
    part_1(ing_ranges, ing_ids)


# part 2


def part_2(irs):

    s = 0

    irs.sort()
    
    while True:
        # print("irs len =", len(irs))
        
        o = False
        for i, ir1 in enumerate(irs):
            for j, ir2 in enumerate(irs):
                if i != j and j > i and ir1[1] >= ir2[0]:
                    irs[i] = (
                        min(ir1[0], ir2[0]),
                        max(ir1[1], ir2[1]),
                    )
                    irs.pop(j)
                    o = True
                    break
            else:
                continue
            break

        if o is False:
            break

    s = 0
    for ir in irs:
        s += ir[1] - (ir[0] - 1)

    print("part_2", s)


with timer("part_2"):
    part_2(ing_ranges)
