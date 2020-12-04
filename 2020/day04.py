import utils
import re

# The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:
# 
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
# 
# Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.
# 
# Here is an example batch file containing four passports:
# 
# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm
# 
# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929
# 
# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm
# 
# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
# 
# Valid, invalid, valid, invalid
# 
# Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

def get_input():
    return utils.get_input(4)


def part1(raw_text):
    # doesn't prevent repeated keys, but ¯\_(ツ)_/¯
    required = "ecl|pid|eyr|hcl|byr|iyr|hgt"
    valid_regex = re.compile(
            r"(?:(?:" + required + r"|cid)(?::\S+)\s){8}\n|(?:(?:" + required + r")(?::\S+)\s){7}\n",
            re.MULTILINE)
    return sum(1 for _ in valid_regex.finditer(raw_text + "\n\n"))


# You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:
# 
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#   If cm, the number must be at least 150 and at most 193.
#   If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
# Your job is to count the passports where all required fields are both present and valid according to the above rules.

def part2(raw_text):
    fields_regex = re.compile(r"(ecl|pid|eyr|hcl|byr|iyr|hgt|cid):(\S+)")
    hcl_regex = re.compile(r"#[0-9a-f]{6}")
    # This is gonna be ugly, but I really want to play with the walrus := operator
    return sum(bool((fields := dict(fields_regex.findall(candidate))) and 7 <= len(fields) <= 8
            and (byr := fields.get("byr")) and byr.isdecimal() and 1920 <= int(byr) <= 2002
            and (iyr := fields.get("iyr")) and iyr.isdecimal() and 2010 <= int(iyr) <= 2020
            and (eyr := fields.get("eyr")) and eyr.isdecimal() and 2020 <= int(eyr) <= 2030
            and (hgt := fields.get("hgt")) and (
                hgt.endswith("cm") and (hgt_n := hgt[:-2]).isdecimal() and 150 <= int(hgt_n) <= 193
                or hgt.endswith("in") and (hgt_n := hgt[:-2]).isdecimal() and 59 <= int(hgt_n) <= 76)
            and (hcl := fields.get("hcl")) and hcl_regex.match(hcl)
            and (ecl := fields.get("ecl")) and ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
            and (pid := fields.get("pid")) and len(pid) == 9 and pid.isdecimal())
            for candidate in raw_text.split("\n\n"))


if __name__ == "__main__":
    print(part1(get_input()))
    print(part2(get_input()))

