# ach Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:
#
# The number of inches between the left edge of the fabric and the left edge of the rectangle.
# The number of inches between the top edge of the fabric and the top edge of the rectangle.
# The width of the rectangle in inches.
# The height of the rectangle in inches.
# A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:
#
# ...........
# ...........
# ...#####...
# ...#####...
# ...#####...
# ...#####...
# ...........
# ...........
# ...........
# The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:
#
# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2
# Visually, these claim the following areas:
#
# ........
# ...2222.
# ...2222.
# .11XX22.
# .11XX22.
# .111133.
# .111133.
# ........
# The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)
#
# If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?

import re
import utils

PATTERN = re.compile(r'#(?P<id>\d+) @ (?P<left>\d+),(?P<top>\d+): (?P<width>\d+)x(?P<height>\d+)')

class Claim:
  def __init__(self, match):
    self.left = int(match.group('left'))
    self.right = int(match.group('width')) + self.left
    self.top = int(match.group('top'))
    self.bottom = int(match.group('height')) + self.top
    self.id = int(match.group('id'))

def part_1(part2=False):
  m_x = 0
  m_y = 0
  claims = [Claim(re.match(PATTERN, claim)) for claim in utils.get_input_lines(3)]
  for claim in claims:
    m_x = max(m_x, claim.right)
    m_y = max(m_y, claim.bottom)
  fabric = [[0 for _ in range(m_y)] for _ in range(m_x)]
  for claim in claims:
    for x in range(claim.left, claim.right):
      for y in range(claim.top, claim.bottom):
        fabric[x][y] += 1

  return sum(fabric[x][y] >= 2 for x in range(m_x) for y in range(m_y))


print(part_1())

# --- Part Two ---

# What is the ID of the only claim that doesn't overlap?

from itertools import product


def part_2():
  claims = [Claim(re.match(PATTERN, claim)) for claim in utils.get_input_lines(3)]

  for a in claims:
    for b in claims:
      if a == b:
        continue
      if ((a.left < b.right) and (a.right > b.left)
          and (a.top < b.bottom) and (a.bottom > b.top)):
        break
    else:
      return a.id


print(part_2())
