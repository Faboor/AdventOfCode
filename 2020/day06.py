import utils
from itertools import chain

# The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.
#
# you write down the questions for which they answer "yes", one per line. For example:
# 
# abcx
# abcy
# abcz
# In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)
# 
# Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line.# For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?


def get_input():
    return chain(utils.get_input_lines_iter(6), [""])


def part1(lines):
    total = 0
    answered = set()
    for line in lines:
        if line:
            answered.update(line)
        else:
            total += len(answered)
            answered = set()
    return total


# You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

def part2(lines):
    total = 0
    base = set("qwertyuiopasdfghjklzxcvbnm")
    answered = base.copy()
    for line in lines:
        if line:
            answered.intersection_update(line)
        else:
            total += len(answered)
            answered = base.copy()
    return total


if __name__ == "__main__":
    print(part1(get_input()))
    print(part2(get_input()))

