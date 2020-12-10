import utils
import day01
from itertools import islice, accumulate, dropwhile

# starts by transmitting a preamble of 25 numbers. After that, each number you receive should be the sum of any two of the 25 immediately previous numbers. The two numbers will have different values, and there might be more than one such pair.
# Here is a larger example which only considers the previous 5 numbers (and has a preamble of length 5):
# 
# 35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576
# In this example, after the 5-number preamble, almost every number is the sum of two of the previous 5 numbers; the only number that does not follow this rule is 127.
# find the first number in the list (after the preamble) which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property?


def get_input():
    return [int(line) for line in utils.get_input_lines_iter(9)]


def part1(lines, window=25):
    i = window + 1
    while day01.part1(islice(lines, i - window, i), target=lines[i]) is not None:
        i += 1
    return lines[i]


# you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.
# Again consider the above example: In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127.
# Add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

def part2(lines, target):
    acc = accumulate(lines)
    seen = {}
    for i, x in enumerate(acc):
        if (y := x - target) in seen:
            break
        seen[x] = i
    subsequence = lines[seen[y] + 1:i + 1]
    return min(subsequence) + max(subsequence)


if __name__ == "__main__":
    target = part1(lines := get_input())
    print(target)
    print(part2(lines, target))

