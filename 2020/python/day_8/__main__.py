from common import get_input, logger

input = [line.partition(" ") for line in get_input().read_text().split("\n")]

logger.info(input)

# oh boy a turing machine


def part_1(input):
    tape = [(element[0], int(element[2])) for element in input]

    acc = 0
    head = 0

    ops = set()

    try:
        while True:
            op, arg = tape[head]
            logger.info("op=%s arg=%s", op, arg)
            match op:
                # set acc and advance the tape
                case "acc":
                    acc += arg
                    head += 1
                # jmp to the arg
                case "jmp":
                    head += arg
                case "nop":
                    head += 1

            if head in ops:
                logger.info(acc)
                break

            ops.add(head)
    except IndexError as err:
        raise err


# part_1(input)


def part_2(input):
    tape = [(element[0], int(element[2])) for element in input]

    acc = 0
    head = 0

    ex = []
    cor = set()
    fixed = None

    try:
        while True:
            op, arg = tape[head]
            logger.info("op=%s arg=%s", op, arg)

            match op:
                # set acc and advance the tape
                case "acc":
                    acc += arg
                    head += 1
                # jmp to the arg
                case "jmp":
                    if fixed is None and head not in cor:
                        fixed = head
                        head += 1
                    else:
                        head += arg

                case "nop":
                    if fixed is None and head not in cor:
                        fixed = head
                        head += arg
                    else:
                        head += 1

            # reset head
            if head in ex:
                acc = 0
                head = 0
                ex = []
                cor.add(fixed)
                fixed = None

            ex.append(head)

            logger.info(cor)

    except IndexError:
        logger.info("solution=%s", acc)


part_2(input)
