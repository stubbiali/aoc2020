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


# >>> utilities
def get_group(lines, start):
    group = []

    while start < len(lines) and lines[start] != "\n":
        group.append(lines[start][:-1])
        start += 1

    return group


def get_group_count(group):
    questions = {letter for letter in group[0]}
    i = 1
    while i < len(group) and len(questions) > 0:
        questions.intersection_update([letter for letter in group[i]])
        i += 1
    return len(questions)


# >>> main
def main(filename):
    with open(filename, "r") as data:
        lines = list(data)

        i = 0
        count = 0

        while i < len(lines):
            group = get_group(lines, i)
            count += get_group_count(group)
            i += len(group) + 1

        print(f"The result is {count}.")


# >>> runtime
if __name__ == "__main__":
    main("input.txt")
