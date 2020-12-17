import utils


def get_input():
    return ((line[0], int(line[1:])) for line in utils.get_input_lines_iter(12))


directions = {
    # dir: (left, right, (dx, dy))
    'E': ('N', 'S', (1, 0)),
    'N': ('W', 'E', (0, 1)),
    'W': ('S', 'N', (-1, 0)),
    'S': ('E', 'W', (0, -1)),
}

def part1(commands):
    x, y = 0, 0
    facing = 'E'
    for cmd, n in commands:
        if (rotation := "LR".find(cmd)) > -1:
            for _ in range(n // 90):
                facing = directions[facing][rotation]
        else:
            direction = directions.get(cmd) or directions[facing]
            x += direction[2][0] * n
            y += direction[2][1] * n
    return abs(x) + abs(y)


def part2(commands):
    x, y = 0, 0
    wx, wy = 10, 1
    for cmd, n in commands:
        if cmd == 'F':
            x += wx * n
            y += wy * n
        elif (direction := directions.get(cmd)):
            wx += direction[2][0] * n
            wy += direction[2][1] * n
        else:
            d = 1 if cmd == 'L' else -1
            for _ in range(n // 90):
                wx, wy = wy * -d, wx * d
    return abs(x) + abs(y)




if __name__ == "__main__":
    print(part1(get_input()))
    print(part2(get_input()))

