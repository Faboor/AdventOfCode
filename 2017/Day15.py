# Generator A and generator B, are trying to agree on a
# sequence of numbers. However, one of them is
# malfunctioning, and so the sequences don't always match.
# As they do this, a judge waits for each of them to
# generate its next value, compares the lowest 16 bits of
# both values, and keeps track of the number of times those
# parts of the values match.
# The generators both work on the same principle. To create
# its next value, a generator will take the previous value
# it produced, multiply it by a factor (generator A uses
# 16807; generator B uses 48271), and then keep the
# remainder of dividing that resulting product by
# 2147483647. That final remainder is the value it produces
# next. To calculate each generator's first value, it
# instead uses a specific starting value as its "previous
# value" (as listed in your puzzle input).
# After 40 million pairs, what is the judge's final count?
M = 2147483647
mask = 65535


class Gen(object):
  def __init__(self, start, factor, filter):
    self.previous = start
    self.factor = factor
    self.filter = filter

  def __next__(self):
    self.previous = (self.previous * self.factor) % M
    while self.previous % self.filter:
      self.previous = (self.previous * self.factor) % M
    return self.previous


def pairs(A, B, limit):
  count = 0
  for i in range(limit):
    count += judge(next(A), next(B))
  return count


def judge(a, b):
  return (a & mask) == (b & mask)


def init_gens(filter_a=1, filter_b=1):
  A = Gen(512, 16807, filter_a)
  B = Gen(191, 48271, filter_b)
  return A, B


# --- Part Two ---
# They still generate values in the same way, but now they
# only hand a value to the judge when it meets their
# criteria:
# - Generator A looks for values that are multiples of 4.
# - Generator B looks for values that are multiples of 8.
# Each generator functions completely independently
# After 5 million pairs, but using this new generator logic,
# what is the judge's final count?

# Modified part 1 to allow filters and different limits

if __name__ == '__main__':
  print(pairs(*init_gens(), limit=(40 * 10**6)))
  print(pairs(*init_gens(4, 8), limit=(5 * 10**6)))
