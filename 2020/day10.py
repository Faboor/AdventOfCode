import utils
from itertools import chain, islice


def get_input():
    return sorted(map(int, utils.get_input_lines(10)))

def part1(adapters):
    counter = [0, 0, 0, 1]
    counter[adapters[0]] += 1
    for x, y in zip(adapters, islice(adapters, 1, len(adapters))):
        counter[y - x] += 1
    return counter[1] * counter[3]


def part2(adapters, max_diff=3):
    options = [1] + [0] * len(adapters)
    adapters = [0] + adapters
    for i, current in enumerate(islice(adapters, 1, len(adapters)), 1):
        options[i] = sum(options[j]
                for j in range(max(0, i - max_diff), i)
                if current - adapters[j] <= max_diff)
    return options[-1]


if __name__ == "__main__":
    print(part1(get_input()))
    print(part2(get_input()))

