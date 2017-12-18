# The depth of each layer and the range of the scanning area
# for the scanner within it, written as depth: range. Each
# layer has a thickness of exactly 1. A layer at depth 0
# begins immediately inside the firewall; a layer at depth 1
#  would start immediately after that.
# 0: 3             0   1   2   3   4   5   6
# 1: 2            [ ] [ ] ... ... [ ] ... [ ]
# 4: 4     ==>    [ ] [ ]         [ ]     [ ]
# 6: 4            [ ]             [ ]     [ ]
#                                 [ ]     [ ]
# Within each layer, a security scanner moves back and forth
# within its range. Each security scanner starts at the top
# and moves down until it reaches the bottom, then moves up
# until it reaches the top, and repeats.
# Your plan is to hitch a ride on a packet about to move
# through the firewall. The packet will travel along the top
# of each layer. The packet moves one layer forward (its
# first move takes it into layer 0), and then the scanners
# move one step.If there is a scanner at the top of the
# layer as your packet enters it, you are caught.(If a
# scanner moves into the top of its layer while you are
# there, you are not caught). In example situation above
# you are caught in layers 0 and 6. The severity of getting
# caught on a layer is equal to its depth multiplied by its
# range. In the example above, the trip severity is
# 0*3 + 6*4 = 24.
# What is the severity of your whole trip?
def severity(scanners, time=0):
  total_severity = 0
  for depth in range(len(scanners)):
    if hit(scanners[depth], time):
      total_severity += depth * scanners[depth]
    time += 1
  return total_severity


def hit(scan, time):
  return scan and not time % (2 * scan - 2)


# --- Part Two ---
# What is the fewest number of picoseconds that you need to
# delay the packet to pass through the firewall without
# being caught?



def get_input():
  scanners = [0] * 100
  with open('inputs/Day13') as f:
    for line in f:
      s = line.split(': ')
      scanners[int(s[0])] = int(s[1])
  return scanners


if __name__ == '__main__':
  print(severity(get_input()))
