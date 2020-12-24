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
def get_positions(line):
    pattern = re.compile(r"([0-9]+)")
    out = pattern.findall(line)
    assert len(out) >= 2
    return int(out[0]) - 1, int(out[1]) - 1


def get_character(line):
    pattern = re.compile(r" ([a-zA-Z]):")
    out = pattern.findall(line)
    assert len(out) > 0
    return out[0]


def assert_password(line, pos, char):
    pattern = re.compile(r": ([a-zA-Z]+)")
    tmp = pattern.findall(line)
    assert len(tmp) == 1
    password = tmp[0]
    out = [password[p] == char if p < len(password) else 2 for p in pos]
    return sum(out) == 1


# >>> main
def main(filename):
    with open(filename, "r") as data:
        data = list(data)

        count = 0

        for line in data:
            pos = get_positions(line)
            char = get_character(line)
            count += assert_password(line, pos, char)

        print(f"The result is {count}.")


# >>> runtime
if __name__ == "__main__":
    main("input.txt")
