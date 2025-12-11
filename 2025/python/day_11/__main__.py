from common import get_input, timer
from functools import lru_cache

input = get_input().read_text().split("\n")
devices = {}
for line in input:
    device, _, outputs = line.partition(": ")
    devices[device] = outputs.split(" ")
#
devices["out"] = []


def part_1(devices):
    paths = 0
    stack = ["you"]
    while len(stack) > 0:
        # print("stack", stack)
        cur = stack.pop()
        outputs = devices[cur]
        for output in outputs:
            if output == "out":
                paths += 1
            else:
                stack.append(output)

    print("part_1", paths)


with timer("part_1"):
    part_1(devices)


# recursion blah
@lru_cache
def paths(start, end) -> int:
    return 1 if start == end else sum(paths(device, end) for device in devices[start])


def part_2(devices):
    p1 = paths("svr", "fft")
    p2 = paths("fft", "dac")
    p3 = paths("dac", "out")

    print("part_2", p1 * p2 * p3)


with timer("part_2"):
    part_2(devices)
