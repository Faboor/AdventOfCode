import utils
from collections import defaultdict, deque


# bags must be color-coded and must contain specific quantities of other color-coded bags
# 
# For example, consider the following rules:
# 
# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# 
# You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)
# 
# So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

def get_input():
    return utils.get_input_lines_iter(7)


def graphs(lines, *, bags_containing=None, bags_contained_in=None):
    bags_containing_dict = defaultdict(list)
    bags_contained_in_dict = defaultdict(list)
    for line in lines:
        outer, inners = line.strip(".").split(" bags contain ")
        inners = [] if inners == "no other bags" else [
                ((num_and_colour := inner.split(" ", 1))[1].rsplit(" ", 1)[0], int(num_and_colour[0]))
                for inner in inners.split(", ")
        ]
        for inner in inners:
            if bags_containing:
                bags_containing_dict[inner[0]].append((outer, inner[1]))
            if bags_contained_in:
                bags_contained_in_dict[outer].append(inner)
    return {"bags_containing": bags_containing_dict, "bags_contained_in": bags_contained_in_dict}


def part1(lines):
    bags_containing = graphs(lines, bags_containing=True)["bags_containing"]
    q = deque([("shiny gold", 1)])
    visited = set()
    while q:
        current = q.pop()[0]
        if current in visited:
            continue
        visited.add(current)
        q.extend(bags_containing[current])
    return len(visited) - 1


# So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!
# How many individual bags are required inside your single shiny gold bag?

def part2(lines):
    bags_contained_in = graphs(lines, bags_contained_in=True)["bags_contained_in"]
    q = deque([("shiny gold", 1)])
    total = 0
    while q:
        current, multiplier = q.pop()
        for colour, number in bags_contained_in[current]:
            colour_total = multiplier * number
            total += colour_total
            q.append([colour, colour_total])
    return total


if __name__ == "__main__":
    print(part1(get_input()))
    print(part2(get_input()))

