import utils
import sys

def get_input():
    time, buses = utils.get_input_lines(13)
    return int(time), buses.split(",")


def part1(time, buses):
    # assumes that no bus leaves directly on `time`
    return (bus := min(map(int, filter("x".__ne__, buses)),
            key=lambda bus: bus - time % bus)) * (bus - time % bus)


def part2(buses):
    # assumes bus ids are coprime
    offset_bus = sorted(map(lambda x: (x[0], int(x[1])),
            filter(lambda x: x[1] != "x", enumerate(buses))),
            key=lambda x: x[1], reverse=True)
    period = offset_bus[0][1]
    current = period - offset_bus[0][0]
    for offset, bus in offset_bus[1:]:
        target_remainder = offset and bus - (offset % bus)
        while current % bus != target_remainder:
            current += period
        period *= bus
    return current


if __name__ == "__main__":
    print(part1(*get_input()))
    print(part2(get_input()[1]))

