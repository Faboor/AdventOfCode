from collections import defaultdict

import utils
from itertools import cycle


class Node:
  def __init__(self, val, prv=None, nxt=None):
    self.val = val
    self.prv = prv or self
    self.nxt = nxt or self

  def insert_next(self, val):
    new_node = Node(val, prv=self, nxt=self.nxt)
    self.nxt.prv = new_node
    self.nxt = new_node
    return new_node

  def remove(self):
    self.nxt.prv = self.prv
    self.prv.nxt = self.nxt
    return self.val, self.nxt

  def insert_one_further(self, val):
    return self.nxt.insert_next(val)

  def remove_seven_back(self):
    return self.prv.prv.prv.prv.prv.prv.prv.remove()


def part_1(a=None):
  players, marbles = a or map(int, utils.get_input(9).split(' ')[::6])
  scores = defaultdict(int)
  current = Node(0)
  for player, marble in zip(cycle(range(1, players + 1)), range(1, marbles + 1)):
    if marble % 23 == 0:
      removed, current = current.remove_seven_back()
      scores[player] += marble + removed
    else:
      current = current.insert_one_further(marble)

  return max(scores.values())


print(part_1())


def part_2():
  players, marbles = map(int, utils.get_input(9).split(' ')[::6])
  return part_1((players, marbles * 100))


print(part_2())
