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
def get_trees(matrix, m, n, dx, dy):
    j = 0
    trees = 0

    for i in range(dx, m):
        j = (j + dy) % n
        trees += matrix[i][j] == "#"

    return trees


# >>> main
def main(filename, right_shift, down_shift):
    with open(filename, "r") as data:
        matrix = list(data)
        m = len(matrix)
        n = len(matrix[0][:-1])

        result = functools.reduce(
            lambda x, y: x * y,
            [
                get_trees(matrix, m, n, dx, dy)
                for dx, dy in zip(down_shift, right_shift)
            ],
            1,
        )

        print(f"The result is {result}.")


# >>> main
if __name__ == "__main__":
    main("input.txt", (3,), (1,))
