from collections import defaultdict as ddict


# Each instruction consists of several parts: the register
# to modify, whether to increase or decrease that
# register's value, the amount by which to increase or
# decrease it, and a condition. If the condition fails,
# skip the instruction without modifying the register.
# The registers all start at 0. The instructions look like
# this:
# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10
# You might also encounter <= (less than or equal to) or
# != (not equal to).
# What is the largest value in any register after completing
# the instructions in your puzzle input?
def simulate(instructions):
  cond = {
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
    '>=': lambda x, y: x >= y,
    '<=': lambda x, y: x <= y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y
  }
  reg = ddict(int)
  maximum = 0
  for instr in instructions:
    instr = instr.split()
    if cond[instr[5]](reg[instr[4]], int(instr[6])):
      reg[instr[0]] += int(instr[2]) if instr[1] == 'inc' else -int(instr[2])
      maximum = max(maximum, reg[instr[0]])
  return reg, maximum


# --- Part Two ---
# What is the highest intermediate value in any register
# during the run of the simulation.

# Modified `simulate` to return maximum


def get_input():
  with open('inputs/Day08') as f:
    return f.read().splitlines()


if __name__ == '__main__':
  regs, maximum = simulate(get_input())
  print(max(regs.values()))
  print(maximum)