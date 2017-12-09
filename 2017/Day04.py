

# A passphrase consists of a series of words (lowercase
#  letters) separated by spaces. A valid passphrase must
# contain no duplicate words. The system's full passphrase
# list is available as your puzzle input. How many
# passphrases are valid?
def no_duplicates(passphrases):
  valid = 0
  for p in passphrases:
    words = p.split(' ')
    unique = set(words)
    valid += len(words) == len(unique)
  return valid


# --- Part Two ---
# For added security, yet another system policy has been
# put in place. Now, a valid passphrase must contain no
# two words that are anagrams of each other. Under this
# new system policy, how many passphrases are valid?
def no_anagrams(passphrases):
  valid = 0
  for p in passphrases:
    words = p.split(' ')
    unique = set(map(lambda w: ''.join(sorted(w)), words))
    valid += len(words) == len(unique)
  return valid


def get_input():
  with open('inputs/Day04') as f:
    return map(lambda x: x[:-1], f.readlines())
