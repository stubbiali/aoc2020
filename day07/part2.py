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
registry = {}


def register_bag(line):
    pattern = re.compile(r"no other bags\.")
    if pattern.findall(line):
        return

    pattern = re.compile(r"^([a-z]+) ([a-z]+) bags")
    matches = pattern.findall(line)
    assert len(matches) == 1
    bag = f"{matches[0][0]}_{matches[0][1]}"
    subbags = registry.setdefault(bag, {})

    pattern = re.compile(r"([0-9]+) ([a-z]+) ([a-z]+) bag")
    matches = pattern.findall(line)
    for match in matches:
        subbag = f"{match[1]}_{match[2]}"
        subbags.setdefault(subbag, 0)
        subbags[subbag] += int(match[0])


def get_count(bag):
    if bag not in registry:
        return 0
    return sum(
        [registry[bag][subbag] * (1 + get_count(subbag)) for subbag in registry[bag]]
    )


# >>> main
def main(filename, target):
    with open(filename, "r") as data:
        lines = list(data)

        for line in lines:
            register_bag(line)

        print(f"The result is {get_count(target)}.")


# >>> runtime
if __name__ == "__main__":
    main("input.txt", "shiny_gold")
