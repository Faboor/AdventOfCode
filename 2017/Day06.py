# In this area, there are sixteen memory banks; each memory
# bank can hold any number of blocks. The goal of the
# reallocation routine is to balance the blocks between the
# memory banks.
# The reallocation routine operates in cycles. In each
# cycle, it finds the memory bank with the most blocks (ties
# won by the lowest-numbered memory bank) and redistributes
# those blocks among the banks. To do this, it removes all of
# the blocks from the selected bank, then moves to the next
# (by index) memory bank and inserts one of the blocks. It
# continues doing this until it runs out of blocks; if it
# reaches the last memory bank, it wraps around to the first
# one.
# The debugger would like to know how many redistributions
# can be done before a blocks-in-banks configuration is
# produced that has been seen before.
def part1(b):
  seen = set()
  cycle = 0
  while tuple(b) not in seen:
    seen.add(tuple(b))
    redis(b)
    cycle += 1
  return cycle


def redis(b):
  mi = max_index(b)
  to_move = b[mi]
  b[mi] = 0
  for i in range(mi + 1, mi + to_move + 1):
    b[i % len(b)] += 1


def max_index(b):
  mi = 0
  for i in range(1, len(b)):
    if b[i] > b[mi]:
      mi = i
  return mi


# --- Part Two ---
# Out of curiosity, the debugger would also like to know
# the size of the loop: starting from a state that has
# already been seen, how many block redistribution cycles
# must be performed before that same state is seen again?
def part2(b):
  cycle = 0
  seen = dict()
  while tuple(b) not in seen:
    seen[tuple(b)] = cycle
    redis(b)
    cycle += 1
  return cycle - seen[tuple(b)]


def get_input():
  with open('inputs/Day06') as f:
    return list(map(int, f.read().split('\t')))


if __name__ == '__main__':
  print(part1(get_input()))
  print(part2(get_input()))