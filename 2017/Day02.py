
# The spreadsheet consists of rows of apparently-random
# numbers. To make sure the recovery process is on the
# right track, they need you to calculate the spreadsheet's
# checksum. For each row, determine the difference between
# the largest value and the smallest value; the checksum is
# the sum of all of these differences.
def checksum(s):
    sum = 0
    for raw_line in s.split('\n'):
        line = list(map(int, raw_line.split('\t')))
        sum += max(line) - min(line)
    return sum


# --- Part Two ---

# It sounds like the goal is to find the only two numbers
# in each row where one evenly divides the other - that is,
# where the result of the division operation is a whole
# number. They would like you to find those numbers on each
# line, divide them, and add up each line's result.
def checksum2(s):
    sum = 0
    for raw_line in s.split('\n'):
        line = list(map(int, raw_line.split('\t')))
        for i, x in enumerate(line, 1):
            for y in line[i:]:
                if not max(x, y) % min(x, y):
                    sum += max(x, y) / min(x, y)
                    break
    return sum


def get_input():
    with open('inputs/Day02') as f:
        return f.read()[:-1]
