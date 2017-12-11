

# Groups - sequences that begin with { and end with }.
# Within a group, there are zero or more other things,
# separated by commas: either another group or garbage.
# Since groups can contain other groups, a } only closes
# the most-recently-opened unclosed group - that is,
# they are nestable. Your puzzle input represents a single,
# large group which itself contains many smaller ones.
# Garbage begins with < and ends with >. Between those
# angle brackets, almost any character can appear,
# including { and }. Within garbage, < has no special
# meaning. In a futile attempt to clean up the garbage,
# some program has canceled some of the characters within
# it using !: inside garbage, any character that comes
# after ! should be ignored, including <, >, and even
# another !.
# Each group is assigned a score which is one more than
# the score of the group that immediately contains it.
# The outermost group gets a score of 1.
# {}, score of 1.
# {{{}}}, score of 1 + 2 + 3 = 6.
# The goal is to find the total score for all groups
def process(s):
  total = 0
  stack = [0]
  garbage = False
  i = 0
  while i < len(s):
    if not garbage:
      if s[i] == '{':
        stack.append(stack[-1] + 1)
      elif s[i] == '}':
        total += stack.pop()
      elif s[i] == '<':
        garbage = True
    else:
      if s[i] == '>':
        garbage = False
      elif s[i] == '!':
        i += 1
    i += 1
  return total


def get_input():
  with open('inputs/Day09') as f:
    return f.read()


if __name__ == '__main__':
  print(*process(get_input()), sep='\n')
