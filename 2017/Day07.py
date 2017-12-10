from collections import defaultdict as ddict


class Node(object):
  def __init__(self, name, weight, child_names):
    self.name = name
    self.weight = weight
    self.child_names = child_names

  @staticmethod
  def from_str(s):
    s = s.split(' ')
    name = s[0]
    weight = int(s[1][1:-1])  # remove brackets
    child_names = []
    if len(s) > 2:
      for child in s[3:]:
        child_names.append(child.replace(',', ''))
    return Node(name, weight, child_names)


# You ask each program to yell out their name, their
# weight, and (if they're holding a disc) the names of
# the programs immediately above them balancing on that
# disc.
#
#                                                      gyxo
#                                                    /
# pbga (66)                                     ugml - ebii
# xhth (57)                                   /      \
# ebii (61)                                  |         jptl
# havc (66)                                  |
# ktlj (57)                                  |         pbga
# fwft (72) -> ktlj, cntj, xhth             /        /
# qoyq (66)                       ==>  tknk --- padx - havc
# padx (45) -> pbga, havc, qoyq             \        \
# tknk (41) -> ugml, padx, fwft              |         qoyq
# jptl (61)                                  |
# ugml (68) -> gyxo, ebii, jptl              |         ktlj
# gyxo (61)                                   \      /
# cntj (57)                                     fwft - cntj
#                                                    \
#                                                      xhth
# What is the name of the bottom program?
def find_root(p):
  for name, parent in p.items():
    if parent is None:
      return name


# --- Part Two ---
# For any program holding a disc, each program standing on
# that disc forms a sub-tower. Each of those sub-towers
# are supposed to be the same weight, or the disc itself
# isn't balanced. The weight of a tower is the sum of the
# weights of the programs in that tower.
# Given that exactly one program is the wrong weight, what
# would its weight need to be to balance the entire tower?
def part2(nodes):
  pass


def get_input():
  nodes = {}
  parent = {}
  with open('inputs/Day07') as f:
    for line in f.read().splitlines():
      node = Node.from_str(line)
      nodes[node.name] = node
      parent.setdefault(node.name, None)
      for child in node.child_names:
        parent[child] = node
  return nodes, parent


if __name__ == '__main__':
    print(find_root(get_input()[1]))
