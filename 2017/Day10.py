# Begin with a list of numbers from 0 to 255, a current
# position which begins at 0 (the first element in the
# list), a skip size (which starts at 0), and a sequence of
# lengths (your puzzle input). Then, for each length:
# - Reverse the order of that length of elements in the
#   list, starting with the element at the current position.
# - Move the current position forward by that length plus
#   the skip size.
# - Increase the skip size by one.
# The list is circular; if the current position and the
# length try to reverse elements beyond the end of the list,
# the operation reverses using as many extra elements as it
# needs from the front of the list. If the current position
# moves past the end of the list, it wraps around to the
# front. Lengths larger than the size of the list are
# invalid.
# What is the result of multiplying the first two numbers
# in the list?
