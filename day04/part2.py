# -*- coding: utf-8 -*-
#
# Advent of Code 2020
#
# Copyright (C) 2020, Stefano Ubbiali
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import re


# >>> utilities
def get_lines(data, start):
    lines = []
    i = start
    while i < len(data) and data[i] != "\n":
        lines.append(data[i])
        i += 1
    return lines


def get_dictionary(lines):
    pattern = re.compile(r"([a-z]+):")
    keys = tuple(key for line in lines for key in pattern.findall(line))

    pattern = re.compile(r":([^ ]+)\b")
    values = tuple(values for line in lines for values in pattern.findall(line))

    assert len(keys) == len(values)

    return {key: value for key, value in zip(keys, values)}


def check_passport(lines):
    required_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

    passport = get_dictionary(lines)

    if not all(required_key in passport for required_key in required_keys):
        return False

    v = passport["byr"]
    if not (len(v) == 4 and re.match(r"[0-9]{4}", v) and 1920 <= int(v) <= 2002):
        return False

    v = passport["iyr"]
    if not (len(v) == 4 and re.match(r"[0-9]{4}", v) and 2010 <= int(v) <= 2020):
        return False

    v = passport["eyr"]
    if not (len(v) == 4 and re.match(r"[0-9]{4}", v) and 2020 <= int(v) <= 2030):
        return False

    v = passport["hgt"]
    if re.match(r"[0-9]*(cm|in)", v):
        if not (
            (len(v) == 5 and v[-2:] == "cm" and 150 <= int(v[:-2]) <= 193)
            or (len(v) == 4 and v[-2:] == "in" and 59 <= int(v[:-2]) <= 76)
        ):
            return False
    else:
        return False

    v = passport["hcl"]
    if not (len(v) == 7 and re.match(r"#[0-9a-f]{6}", v)):
        return False

    v = passport["ecl"]
    if not v in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return False

    v = passport["pid"]
    return bool(len(v) == 9 and re.match(r"[0-9]{9}", v))


# >>> main
def main(filename):
    with open(filename, "r") as data:
        data = list(data)

        count = 0
        i = 0
        while i < len(data):
            lines = get_lines(data, i)
            count += check_passport(lines)
            i += len(lines) + 1

        print(f"The result is {count}.")


if __name__ == "__main__":
    main("input.txt")
