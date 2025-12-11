from common import get_input, timer

input = get_input().read_text().split("\n")
devices = {}
for line in input:
    device, _, outputs = line.partition(": ")
    devices[device] = outputs.split(" ")
# print(devices)


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

    print("paths", paths)


with timer("part_1"):
    part_1(devices)
