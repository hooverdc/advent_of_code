from common import get_input, logger

input = [int(line) for line in get_input().read_text().split("\n")]

logger.info(input)

def part_1(input):
    for i_x, i in enumerate(input):
        for j in input[i_x:]:
            if i+j == 2020:
                logger.info("i=%s j=%s s=%s", i,j,i+j)
                logger.info("solution=%s", i*j)
                break

part_1(input)

def part_2(input):
    for i_x, i in enumerate(input):
        for j_x, j in enumerate(input[i_x:]):
            for k in input[j_x:]:
                if i+j+k == 2020:
                    logger.info("i=%s j=%s s=%s", i,j,i+j+k)
                    logger.info("solution=%s", i*j*k)
                    break

part_2(input)