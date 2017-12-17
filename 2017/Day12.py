

# You walk through the village and record the ID of each
# program and the IDs with which it can communicate
# directly (your puzzle input). Each program has one or
# more programs with which it can communicate, and these
# pipes are bidirectional; if 8 says it can communicate
# with 11, then 11 will say it can communicate with 8.
# 0 <-> 2
# 1 <-> 1
# 2 <-> 0, 3, 4
# 3 <-> 2, 4
# 4 <-> 2, 3, 6
# 5 <-> 6
# 6 <-> 4, 5
# You need to figure out how many programs are in the group
# that contains program ID 0.
def group(d, start=0):
  visited = {start}
  to_visit = [d[start]]
  while to_visit:
    for x in to_visit.pop():
      if x not in visited:
        visited.add(x)
        to_visit.append(d[x])
  return visited


# --- Part Two ---
# How many groups are there in total?
def groups_count(d):
  unvisited = set(d.keys())
  count = 0
  while unvisited:
    count += 1
    unvisited.difference_update(group(d, unvisited.pop()))
  return count


def get_input():
  d = {}
  with open('inputs/Day12') as f:
    for line in f:
      s = line.split(' <-> ')
      d[int(s[0])] = list(map(int, s[1].split(', ')))
  return d


if __name__ == '__main__':
  d = get_input()
  print(len(group(d, 0)))
  print(groups_count(d))
