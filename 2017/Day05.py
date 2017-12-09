

# An urgent interrupt arrives from the CPU: it's trapped
# in a maze of jump instructions, and it would like
# assistance from any programs with spare cycles to help
# find the exit.
# The message includes a list of the offsets for each jump.
# Jumps are relative: -1 moves to the previous instruction,
# and 2 skips the next one. Start at the first instruction
# in the list. The goal is to follow the jumps until one
# leads outside the list.
# In addition, these instructions are a little strange;
# after each jump, the offset of that instruction
# increases by 1. So, if you come across an offset of 3,
# you would move three instructions forward, but change it
# to a 4 for the next time it is encountered.
# How many steps does it take to reach the exit?
def steps(a):
  nxt = 0
  size = len(a)
  step = 0
  while 0 <= nxt < size:
    tmp = nxt
    nxt += a[nxt]
    a[tmp] += 1
    step += 1
  return step


# --- Part Two ---
# Now, the jumps are even stranger: after each jump, if
# the offset was three or more, instead decrease it by 1.
# Otherwise, increase it by 1 as before.
def steps2(a):
  nxt = 0
  size = len(a)
  step = 0
  while 0 <= nxt < size:
    tmp = nxt
    nxt += a[nxt]
    a[tmp] += 1 if a[tmp] < 3 else -1
    step += 1
  return step


def get_input():
  with open('inputs/Day05') as f:
    return list(map(int, f.readlines()))


if __name__ == '__main__':
  print(steps(get_input()))
  print(steps2(get_input()))