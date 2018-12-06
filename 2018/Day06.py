# The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe or dangerous? It recommends you check manual page 729. The Elves did not give you a manual.
#
# If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives the largest distance from the other points.
#
# Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).
#
# Your goal is to find the size of the largest area that isn't infinite. For example, consider the following list of coordinates:
#
# 1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9
# If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:
#
# ..........
# .A........
# ..........
# ........C.
# ...D......
# .....E....
# .B........
# ..........
# ..........
# ........F.
# This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan distance, each location's closest coordinate can be determined, shown here in lowercase:
#
# aaaaa.cccc
# aAaaa.cccc
# aaaddecccc
# aadddeccCc
# ..dDdeeccc
# bb.deEeecc
# bBb.eeee..
# bbb.eeefff
# bbb.eeffff
# bbb.ffffFf
# Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.
#
# In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their areas extend forever outside the visible grid. However, the areas of coordinates D and E are finite: D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself). Therefore, in this example, the size of the largest area is 17.
#
# What is the size of the largest area that isn't infinite?

import utils
from typing import Dict, Tuple, Iterable, List
from collections import Counter


def m_dist(a, b):
  if not a or not b:
    return float('inf')
  return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part_1():
  points: Dict[int, Tuple[int, int]] = {
    i: tuple(int(coord) for coord in line.split(', '))
    for i, line in enumerate(utils.get_input_lines(6), 10)}
  max_x = max(x for (x, _) in points.values())
  max_y = max(y for (_, y) in points.values())
  board: List[List[int]] = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

  q: Iterable[Tuple[int, Tuple[int, int]]] = points.items()
  next_q: List[Tuple[int, Tuple[int, int]]] = []
  while q:
    for origin_id, p in q:
      occupied_by = board[p[1]][p[0]]
      if not occupied_by:
        board[p[1]][p[0]] = origin_id
        if p[0] > 0:
          next_q.append((origin_id, (p[0] - 1, p[1])))
        if p[0] < max_x:
          next_q.append((origin_id, (p[0] + 1, p[1])))
        if p[1] > 0:
          next_q.append((origin_id, (p[0], p[1] - 1)))
        if p[1] < max_y:
          next_q.append((origin_id, (p[0], p[1] + 1)))
      else:
        if (occupied_by != -1 and origin_id != occupied_by and
            m_dist(p, points[occupied_by]) == m_dist(p, points[origin_id])):
          board[p[1]][p[0]] = -1
    q = next_q
    next_q = []

  to_remove = {-1}
  for x in range(max_x + 1):
    to_remove.add(board[0][x])
    to_remove.add(board[max_y][x])
  for y in range(max_y + 1):
    to_remove.add(board[y][0])
    to_remove.add(board[y][max_x])

  counter = Counter()
  for row in board:
    counter.update(row)
  for r in to_remove:
    counter.pop(r)

  return counter.most_common(1)[0][1]


# --- Part Two ---

# For example, suppose you want the sum of the Manhattan distance to all of the coordinates to be less than 32. For each location, add up the distances to all of the given coordinates; if the total of those distances is less than 32, that location is within the desired region. Using the same coordinates as above, the resulting region looks like this:
#
# ..........
# .A........
# ..........
# ...###..C.
# ..#D###...
# ..###E#...
# .B.###....
# ..........
# ..........
# ........F.
# In particular, consider the highlighted location 4,3 located at the top middle of the region. Its calculation is as follows, where abs() is the absolute value function:
#
# Distance to coordinate A: abs(4-1) + abs(3-1) =  5
# Distance to coordinate B: abs(4-1) + abs(3-6) =  6
# Distance to coordinate C: abs(4-8) + abs(3-3) =  4
# Distance to coordinate D: abs(4-3) + abs(3-4) =  2
# Distance to coordinate E: abs(4-5) + abs(3-5) =  3
# Distance to coordinate F: abs(4-8) + abs(3-9) = 10
# Total distance: 5 + 6 + 4 + 2 + 3 + 10 = 30
# Because the total distance to all coordinates (30) is less than 32, the location is within the region.
#
# This region, which also includes coordinates D and E, has a total size of 16.
#
# Your actual region will need to be much larger than this example, though, instead including all locations with a total distance of less than 10000.
#
# What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?


# What's the maximum this can be? (dm := max_total_distance; n := number of original points)
# If all original points where on (0, 0), then minimum possible x coordinate would be dm / n,
# because every step would increase my total distance by n
# Therefore upper bound for the region to check can be (-dm/n, -dm/n), (max_x + dm/n, max_y + dm/n))
# For this problem thats (-200, -200), (550, 550); thats only 750^2 = 562500 locations
# multiplied by n is ~28 million distance calculations - that's easily brute forced in few seconds

from itertools import product


def part_2():
  points = [tuple(int(coord) for coord in line.split(', ')) for line in utils.get_input_lines(6)]
  min_x = min(x for (x, _) in points)
  max_x = max(x for (x, _) in points)
  min_y = min(y for (_, y) in points)
  max_y = max(y for (_, y) in points)

  return sum(sum(m_dist(candidate, p) for p in points) < 10000
             for candidate
             in product(range(min_x - (10000 // len(points)), max_x + 1 + (10000 // len(points))),
                        range(min_y - (10000 // len(points)), max_y + 1 + (10000 // len(points)))))
