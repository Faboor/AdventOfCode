from collections import defaultdict as dd


# Each square on the grid is allocated in a spiral pattern
# starting at a location marked 1 and then counting up
# while spiraling outward. For example, the first few
# squares are allocated like this:
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...
# While this is very space-efficient (no squares are
# skipped), requested data must be carried back to square
# 1 (the location of the only access port for this memory
# system) by programs that can only move up, down, left,
# or right. They always take the shortest path: the
# Manhattan Distance between the location of the data and
# square 1.
def find_coords(n):

  # Find layer
  layer = 0
  layer_size = 1
  area = 1
  while area < n:
    layer += 1
    layer_size = 8 * layer
    area += layer_size
  coords = [layer, -layer]

  # Backtrack through layer to find n
  for v in [(-1, 0),
            (0, 1),
            (1, 0),
            (0, -1)]:
    for _ in range(int(layer_size / 4)):
      if area == n:
        return coords
      area -= 1
      coords[0] += v[0]
      coords[1] += v[1]
  raise RuntimeError('Something failed')


def Man_dist(c):
  return abs(c[0]) + abs(c[1])


# --- Part Two ---
# As a stress test on the system, the programs here clear
# the grid and then store the value 1 in square 1. Then,
# in the same allocation order as shown above, they store
# the sum of the values in all adjacent squares, including
# diagonals.
# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...
# What is the first value written that is larger than your
# puzzle input?
def part2(n):
  if n == 0:
    return 1
  mem = dd(int)
  mem[0, 0] = 1
  direction = [(0, 1),
               (-1, 0),
               (0, -1),
               (1, 0)]
  coords = (1, -1)
  layer = 1
  while True:
    layer_size = 8 * layer
    for v in direction:
      for _ in range(int(layer_size / 4)):
        coords = (coords[0] + v[0], coords[1] + v[1])
        s = sum_around(coords, mem)
        if s > n:
          return s
        mem[coords] = s
    coords = (coords[0] + 1, coords[1] - 1)
    layer += 1


def sum_around(c, mem):
  s = 0
  for x in range(c[0] - 1, c[0] + 2):
    for y in range(c[1] - 1, c[1] + 2):
      s += mem[x, y]
  return s


def get_input():
  with open('inputs/Day03') as f:
    return int(f.read())
