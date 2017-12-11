from collections import defaultdict as ddict


def reduce(hist):
  for a, b in [('ne', 'sw'), ('n', 's'), ('nw', 'se')]:
    red = min(hist[a], hist[b])
    hist[a] -= red
    hist[b] -= red
  for a, b, c in [
      ('ne', 'nw', 'n'),
      ('ne', 's', 'se'),
      ('n', 'sw', 'nw'),
      ('n', 'se', 'ne'),
      ('nw', 's', 'sw'),
      ('se', 'sw', 's')]:
    red = min(hist[a], hist[b])
    hist[a] -= red
    hist[b] -= red
    hist[c] += red


def dist(s):
  hist = ddict(int)
  for direction in s.split(','):
    hist[direction] += 1
  reduce(hist)
  return sum(hist.values())


def furthest(s):
  hist = ddict(int)
  maximum = 0
  for direction in s.split(','):
    hist[direction] += 1
    reduce(hist)
    maximum = max(maximum, sum(hist.values()))
  return maximum


def get_input():
  with open('inputs/Day11') as f:
    return f.read()[:-1]


if __name__ == '__main__':
  print(dist(get_input()))
  print(furthest(get_input()))
