
# The captcha requires you to review a sequence of digits
# (your puzzle input) and find the sum of all digits that
# match the next digit in the list. The list is circular,
# so the digit after the last digit is the first digit in
# the list.
def sum_if_matches_forward(a, jump=1):
    return sum(map(lambda x: int(x[0]), filter(lambda x: x[0] == x[1], zip(a, a[jump:] + a[:jump]))))


# --- Part Two ---

# Now, instead of considering the next digit, it wants you
# to consider the digit halfway around the circular list.
# That is, if your list contains 10 items, only include
# a digit in your sum if the digit 10/2 = 5 steps forward
# matches it. Fortunately, your list has an even number of
# elements.

# Implemented by adding jump argument
def part2(a):
    return sum_if_matches_forward(a, int(len(a) / 2))


def get_input():
    with open('inputs/Day01') as f:
        return f.read()[:-1]

