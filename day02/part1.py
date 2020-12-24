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
import re


# >>> utilities
def get_range(line):
    pattern = re.compile(r"([0-9]+)")
    out = pattern.findall(line)
    assert len(out) >= 2
    return int(out[0]), int(out[1])


def get_character(line):
    pattern = re.compile(r" [a-zA-Z]:")
    out = pattern.findall(line)
    assert len(out) > 0
    return out[0][1]


def get_occurrences(line, character):
    pattern = re.compile(rf"{character}")
    out = pattern.findall(line)
    assert len(out) > 0
    return len(out) - 1


# >>> main
def main(filename):
    with open(filename, "r") as data:
        data = list(data)

        count = 0

        for line in data:
            cmin, cmax = get_range(line)
            char = get_character(line)
            count += cmin <= get_occurrences(line, char) <= cmax

        print(f"The result is {count}.")


# >>> runtime
if __name__ == "__main__":
    main("input.txt")
