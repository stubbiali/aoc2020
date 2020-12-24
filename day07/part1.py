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
    pattern = re.compile(r"([a-z]+) ([a-z]+) bag")
    bags = pattern.findall(line)
    if len(bags) > 1:
        contained_bags = registry.setdefault(f"{bags[0][0]}_{bags[0][1]}", set())
        for contained_bag in bags[1:]:
            contained_bags.add(f"{contained_bag[0]}_{contained_bag[1]}")


def search_bag(target, source):
    if source not in registry:
        return False
    if target in registry[source]:
        return True
    for bag in registry[source]:
        if search_bag(target, bag):
            return True
    return False


# >>> main
def main(filename, target):
    with open(filename, "r") as data:
        lines = list(data)

        for line in lines:
            register_bag(line)

        count = 0
        for source in registry:
            if source != target:
                count += search_bag(target, source)

        print(f"The answer is {count}.")


# >>> runtime
if __name__ == "__main__":
    main("input.txt", "shiny_gold")
