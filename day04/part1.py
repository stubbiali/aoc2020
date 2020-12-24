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


def get_keys(lines):
    pattern = re.compile(r"([a-z]+):")
    keys = tuple(key for line in lines for key in pattern.findall(line))
    return keys


def check_passport(lines):
    required_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    keys = get_keys(lines)
    out = all(required_key in keys for required_key in required_keys)
    return out


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


# >>> runtime
if __name__ == "__main__":
    main("input.txt")
