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
def validate_number(data, lineno, depth):
    assert lineno < len(data)
    assert lineno - depth >= 0
    s = int(data[lineno])
    for i in range(depth - 1):
        a = int(data[lineno - i - 1])
        for j in range(i, depth):
            b = int(data[lineno - j - 1])
            if a != b and a + b == s:
                return 1
    return 0


# >>> main
def main(filename, depth):
    with open(filename, "r") as data:
        data = list(data)

        for k in range(depth, len(data)):
            if not validate_number(data, k, depth):
                print(f"The result is {int(data[k])}.")
                return

        raise RuntimeError("Fail.")


# >>> runtime
if __name__ == "__main__":
    main("input.txt", 25)
