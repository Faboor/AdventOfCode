import utils

# To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.
# 
# For example, suppose you have the following list:
# 
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

# How many passwords are valid according to their policies?


def get_input():
    for line in utils.get_input_lines(2):
        policy, password = line.split(": ")
        bounds, letter = policy.split(" ")
        first, second = bounds.split("-")
        yield int(first), int(second), letter, password


def part1(lines):
    return sum(low <= password.count(letter) <= high for low, high, letter, password in lines)


# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter.
# How many passwords are valid according to the new interpretation of the policies?

def part2(lines):
    return sum((password[i - 1] == letter) ^ (password[j - 1] == letter)
            for i, j, letter, password in lines)


if __name__ == "__main__":
    print(part1(get_input()))
    print(part2(get_input()))

