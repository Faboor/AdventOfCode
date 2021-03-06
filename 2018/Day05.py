# The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of the same type and opposite polarity are destroyed. Units' types are represented by letters; units' polarity is represented by capitalization. For instance, r and R are units with the same type but opposite polarity, whereas r and s are entirely different types and do not react.
#
# For example:
#
# In aA, a and A react, leaving nothing behind.
# In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
# In abAB, no two adjacent units are of the same type, and so nothing happens.
# In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.
# Now, consider a larger example, dabAcCaCBAcCcaDA:
#
# dabAcCaCBAcCcaDA  The first 'cC' is removed.
# dabAaCBAcCcaDA    This creates 'Aa', which is removed.
# dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
# dabCBAcaDA        No further actions can be taken.
# After all possible reactions, the resulting polymer contains 10 units.
#
# How many units remain after fully reacting the polymer you scanned?

import utils


def part_1():
  result = react(map(ord, utils.get_input(5)))
  return len(result) - 1


def react(ords):
  result = [ord('|')]
  for c in ords:
    if abs(result[-1] - c) == 32:
      result.pop(-1)
    else:
      result.append(c)
  return result


print(part_1())

# --- Part Two ---

# One of the unit types is causing problems; it's preventing the polymer from collapsing as much as it should. Your goal is to figure out which unit type is causing the most problems, remove all instances of it (regardless of polarity), fully react the remaining polymer, and measure its length.
#
# For example, again using the polymer dabAcCaCBAcCcaDA from above:
#
# Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer produces dbCBcD, which has length 6.
# Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer produces daCAcaDA, which has length 8.
# Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer produces daDA, which has length 4.
# Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer produces abCBAc, which has length 6.
# In this example, removing all C/c units was best, producing the answer 4.
#
# What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?

from collections import Counter


def part_2():
  polymer = utils.get_input(5)
  ord_polymer = [ord(x) for x in polymer]
  return min(len(react(filter(not_upper_or_lower(c), ord_polymer)))
             for c in set(polymer.lower())) - 1


def not_upper_or_lower(c):
  c = ord(c)

  def wrapped(x):
    return x != c and x != (c - 32)

  return wrapped


print(part_2())
