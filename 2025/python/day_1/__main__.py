from common import get_input

input = get_input()
rotations = []
d = {"L": -1, "R": 1}
for line in input.read_text().split("\n"):
    if not line:
        continue

    rotations.append(d[line[0]] * int(line[1:]))


def part_1(rotations):
    pos = 50
    n_zeros = 0

    for rotation in rotations:
        # mod 100 gives us end pos
        pos = (rotation + pos) % 100
        if pos == 0:
            n_zeros += 1

    print("part 1:", n_zeros)


part_1(rotations)


def part_2(rotations):
    pos = 50
    n_zeros = 0

    for rotation in rotations:
        # now many N*100 turns do we make to start from R
        n_zeros += abs(rotation) // 100

        # what's left after we take out N*100 from R
        rem = abs(rotation) % 100

        # or we moving left or right
        direction = -1 if rotation < 0 else 1

        # Any case where R isn't N*100 starting from N*100 I think
        if rem > 0:
            # We need the sign and the remainder to figure out our dial end pos
            end_pos = pos + direction * rem

            # If R, and end pos >= 100, we crossed zero again
            # If L, and end_pos is 0 or less, we crossed zero again, but we can overcount if pos was zero
            #
            if (direction > 0 and end_pos >= 100) or (
                direction < 0 and end_pos < 1 and pos > 0
            ):
                n_zeros += 1

            # mod 100 gives us end pos
            pos = end_pos % 100

    print("part 2:", n_zeros)


part_2(rotations)
