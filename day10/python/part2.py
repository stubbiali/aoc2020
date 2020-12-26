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
import functools


# >>> utilities
def get_arrangements_naive(jolts, max_delta):
    if len(jolts) <= 1:
        return 0

    if len(jolts) == 2:
        return 0 <= jolts[1] - jolts[0] <= max_delta

    i = 1
    count = 0
    while i < len(jolts) and jolts[i] - jolts[0] <= max_delta:
        count += get_arrangements_naive(jolts[i:], max_delta)
        i += 1
    return count


def get_arrangements(jolts, max_delta):
    @functools.lru_cache
    def core(start=0):
        sublist = jolts[start:]

        if len(sublist) <= 1:
            return 0

        if len(sublist) == 2:
            return jolts[1] - jolts[0] <= max_delta

        i = 1
        items = []
        while i < len(sublist) and sublist[i] - sublist[0] <= max_delta:
            items.append(sublist[i])
            i += 1

        if i == len(sublist):
            return 2 ** (i - 1)

        count = 0
        for j in range(1, i):
            count += core(start + j)
        return count

    return core()


# >>> main
def main(filename, max_delta):
    with open(filename, "r") as data:
        jolts = sorted(list(int(line) for line in data))
        jolts = [0, *jolts, jolts[-1] + 3]
        print(f"The result is {get_arrangements(jolts, max_delta)}.")


# >> runtime
if __name__ == "__main__":
    main("../input.txt", 3)
