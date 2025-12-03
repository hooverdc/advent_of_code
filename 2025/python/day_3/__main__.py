from common import get_input, timer
from typing import List

input = [[int(c) for c in s] for s in get_input().read_text().split("\n")]


def part_n(input, n):
    sol = 0

    for bank in input:

        h = 0
        c = 0

        j: List[int] = []

        while len(j) < n:
            j.append(bank[h])
            for idx, bat in enumerate(bank):
                if idx < h:
                    continue
                if bat > j[c] and ((len(bank) - 1) - idx) >= (n - (c + 1)):
                    j[c] = bat
                    h = idx
            h += 1
            c += 1
        sol += int("".join(str(i) for i in j))
    return sol


def part_1(input):
    print("part_1", part_n(input, 2))


with timer():
    part_1(input)


def part_2(input):
    print("part_2", part_n(input, 12))


with timer():
    part_2(input)
