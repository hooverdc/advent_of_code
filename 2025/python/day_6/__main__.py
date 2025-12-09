import operator
from common import get_input
from functools import reduce
import re

ops = {
    "+": operator.add,
    "*": operator.mul,
}


def calc(problems):
    s = 0
    for problem in problems:
        t = reduce(
            ops[problem[0]],
            [int(s) for s in problem[1:]],
            0 if problem[0] == "+" else 1,
        )
        s += t
    return s


input = [
    [s for s in line.split(" ") if s != ""]
    for line in get_input().read_text().split("\n")
]

# flip 'em
xl = len(input[0])
yl = len(input)

problems = []
for i in range(xl):
    problem = [*[input[-1][i]], *[input[j][i] for j in range(yl - 1)]]
    problems.append(problem)


print("part_1", calc(problems))

# reset input for part 2 blaaah
# can use the ops as aligners
# remove last space from each expect the last one b/c of the single space col
# guh
lines = get_input().read_text().split("\n")
res = re.findall(r"[\*\+]\s+", lines[-1])
offsets = [*[len(col) - 1 for col in res[:-1]], *[len(res[-1])]]
lines = [line.replace(" ", "0") for line in lines]
problems = []
h = 0
for offset in offsets:
    problem = [line[h : h + offset] for line in lines[:-1]]
    op = lines[-1][h : h + offset][0]
    # rotate -90 deg
    # ex 3x4 > 4x3
    np = [["0" for _ in range(len(problem))] for _ in range(len(problem[0]))]
    for i, row in enumerate(problem):
        for j, col in enumerate(row):
            np[len(col) - j][i] = col
    problems.append([*[op], *[int("".join(s for s in r if s != "0")) for r in np]])
    h += offset + 1

print("part_2", calc(problems))
