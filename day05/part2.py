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
def binary_search(substr, char):
    n = len(substr)
    a = 0
    b = 2 ** n
    c = (a + b) // 2
    for i in range(n):
        if substr[i] == char:
            b = c
            c = (a + c) // 2
        else:
            a = c
            c = (b + c) // 2
    assert b - a == 1
    return a if a == c else b


def get_row(line):
    return binary_search(line[:7], "F")


def get_col(line):
    return binary_search(line[7:10], "L")


def get_seat_id(line):
    return get_row(line) * 8 + get_col(line)


# >>> main
def main(filename):
    with open(filename, "r") as data:
        lines = list(data)

        available_seats = {i for i in range(127 * 8 + 8)}

        for line in lines:
            available_seats.remove(get_seat_id(line))

        left_seats = list(available_seats)
        for i in range(1, len(left_seats) - 1):
            if (
                left_seats[i - 1] + 1 != left_seats[i]
                and left_seats[i] != left_seats[i + 1] - 1
            ):
                print(f"The result is {left_seats[i]}.")


# >>> runtime
if __name__ == "__main__":
    main("input.txt")
