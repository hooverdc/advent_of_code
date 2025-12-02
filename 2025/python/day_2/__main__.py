from common import get_input

input = [[int(x) for x in line.split("-")] for line in get_input().read_text().split(",")]

def part_1(input):
    sol = 0

    for seq in input:
        start, end = seq
        for i in range(start, end+1):
            s = [int(c) for c in str(i)]
            # uneven
            d = len(s)
            if d % 2 == 1:
                continue
            fh, sh = s[:d // 2], s[d // 2:]

            if fh == sh:
                sol += i
    
    print("part 1", sol)

part_1(input)

def part_2(input):
    sol = 0

    for seq in input:
        start, end = seq
        for i in range(start, end+1):
            s = [int(c) for c in str(i)]
            d = len(s)
            for x in range(1, (d // 2) + 1):
                if d % x != 0:
                    continue

                c = []
                for y in range(0, d, x):
                    c.append(s[y:y+x])

                if all([c[0] == n for n in c[1:]]):
                    sol += i
                    break

    print("part 2", sol)

part_2(input)

