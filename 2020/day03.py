import utils
from itertools import count
from math import prod

# A map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:
# 
# ..##.......
# #...#...#..
# .#....#..#.
# ..#.#...#.#
# .#...##..#.
# ..#.##.....
# .#.#.#....#
# .#........#
# #.##...#...
# #...##....#
# .#..#...#.#
# These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:
# 
# You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).
# 
# The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:
# 
# From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map
# 
# In this example, traversing the map using this slope would cause you to encounter 7 trees.


def get_input():
    return list(utils.get_input_lines(3))


def part1(grid, right=3, down=1):
    height = len(grid)
    width = len(grid[0])
    return sum(grid[y][x % width] == "#"
            for x, y in zip(count(0, right), range(0, height, down)))


# Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:
# 
# Righm 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.
# 
# What do you get if you multiply together the number of trees encountered on each of the listed slopes?

def part2(grid):
    slopes = (
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2)
    )
    return prod(part1(grid, right, down) for right, down in slopes)


if __name__ == "__main__":
    print(part1(get_input()))
    print(part2(get_input()))
