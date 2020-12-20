import utils
from itertools import product

def get_input():
    return [line.split(" = ") for line in utils.get_input_lines_iter(14)]


def part1(lines):
    mem = {}
    for cmd, operand in lines:
        if cmd == "mask":
            mask_0 = int(operand.replace("X", "1"), 2)
            mask_1 = int(operand.replace("X", "0"), 2)
        else:
            mem[cmd[4:-1]] = int(operand) & mask_0 | mask_1
    return sum(mem.values())


def part2(lines):
    mem = {}
    for cmd, operand in lines:
        if cmd == "mask":
            mask = operand
            xs = mask.count("X")
        else:
            address = bin(int(cmd[4:-1]))[2:].zfill(36)
            address = "".join(
                    address[i] if m == "0" else "1" if m == "1" else r"{}"
                    for i, m in enumerate(mask))
            for option in product(["0", "1"], repeat=xs):
                mem[int(address.format(*option))] = int(operand)
    return sum(mem.values())



if __name__ == "__main__":
    print(part1(get_input()))
    print(part2(get_input()))

