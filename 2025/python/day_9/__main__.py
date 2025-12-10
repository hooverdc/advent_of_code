from common import get_input, timer
from itertools import combinations
import math

input = [
    tuple([int(s) for s in line.split(",")])
    for line in get_input().read_text().split("\n")
]
pairs = list(combinations(input, 2))


def part_1(pairs):
    largest_area = 0
    for pair1, pair2 in pairs:
        l1 = abs(pair1[0] - pair2[0]) + 1
        l2 = abs(pair1[1] - pair2[1]) + 1

        area = l1 * l2
        # print(pair1, pair2, l1, l2, area)
        if area > largest_area:
            largest_area = area

    print("part_1", largest_area)


with timer("part 1"):
    part_1(pairs)
