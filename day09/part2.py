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
def validate_number(data, k, depth):
    assert k < len(data)
    assert k - depth >= 0
    s = data[k]
    for i in range(depth - 1):
        a = int(data[k - i - 1])
        for j in range(i, depth):
            b = int(data[k - j - 1])
            if a != b and a + b == s:
                return 1
    return 0


def get_range(data, target):
    start = 0
    stop = 1
    while start < len(data) - 1 and stop < len(data):
        s = sum(data[start : stop + 1])
        if s == target:
            return start, stop
        elif s > target:
            start += 1
        else:
            stop += 1
    assert False, "Range not found."


# >>> main
def main(filename, depth):
    with open(filename, "r") as data:
        data = list(data)
        data = list(int(el) for el in data)

        target = None
        for k in range(depth, len(data)):
            if not validate_number(data, k, depth):
                target = data[k]
        if target is None:
            raise RuntimeError("Fail: Target not found.")

        start, stop = get_range(data, target)
        out = min(data[start : stop + 1]) + max(data[start : stop + 1])
        print(f"The result is {out}.")


# >>> runtime
if __name__ == "__main__":
    main("input.txt", 25)
