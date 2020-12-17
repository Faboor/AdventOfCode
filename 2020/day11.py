import utils
from itertools import product

def get_input():
    return utils.get_input_lines(11)


def simulate(seats, threshold, count_occupied):
    change = True
    height = len(seats)
    width = len(seats[0])
    while change:
        change = False
        new_seats = [None] * height
        for y in range(height):
            new_row = [None] * width
            for x in range(width):
                new = current = seats[y][x]
                
                if current != '.':
                    occupied = count_occupied(seats, x, y)
                    if current == 'L' and occupied == 0:
                        new = '#'
                    elif current == '#' and occupied >= threshold:
                        new = 'L'
                change |= current != new
                new_row[x] = new
            new_seats[y] = new_row
        seats = new_seats
    return sum(row.count('#') for row in seats)


def part1(seats):
    height = len(seats)
    width = len(seats[0])
    def occupied_around(seats, x, y):
        return sum(seats[yy][xx] == '#'
                for yy in range(max(0, y - 1), min(height, y + 2))
                for xx in range(max(0, x - 1), min(width, x + 2))
                if yy != y or xx != x)

    return simulate(seats, 4, occupied_around)


def part2(seats):
    height = len(seats)
    width = len(seats[0])
    directions = list(product((-1, 0, 1), repeat=2))
    directions.remove((0, 0))
    def sees_occupied(seats, x, y):
        occupied = 0
        x0, y0 = x, y
        for dx, dy in directions:
            x, y = x0, y0
            while 0 <= (x + dx) < width and 0 <= (y + dy) < height:
                if seats[(y := y + dy)][(x := x + dx)] != '.':
                    break
            occupied += seats[y][x] == '#' and (x != x0 or y != y0)
            if occupied > 5:
                break
        return occupied
    return simulate(seats, 5, sees_occupied)


if __name__ == "__main__":
    print(part1(get_input()))
    print(part2(get_input()))
    
