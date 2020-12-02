import utils

# Before yeu leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.
# 
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
# 
# For example, suppose your expense report contained the following:
# 
# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.


def get_input():
    return map(int, utils.get_input_lines(1))


def part1(numbers, target=2020):
    seen = set()
    for x in numbers:
        if (y := target - x) in seen:
            return x * y
        seen.add(x)

# Same with 3 numbers

def part2(numbers):
    numbers = list(numbers)
    for x in numbers:
        if (ans := part1(numbers, 2020 - x)):
            return x * ans

if __name__ == "__main__":
    print(part1(get_input()))
    print(part2(get_input()))

