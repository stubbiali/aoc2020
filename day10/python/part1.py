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


# >>> main
def main(filename):
    with open(filename, "r") as data:
        jolts = sorted(list(int(line) for line in data))
        d1 = jolts[0] == 1
        d3 = 1
        for i in range(len(jolts) - 1):
            d = jolts[i + 1] - jolts[i]
            assert 0 <= d <= 3
            if d == 1:
                d1 += 1
            elif d == 3:
                d3 += 1
        print(f"The result is {d1*d3}.")


# >>> runtime
if __name__ == "__main__":
    main("../input.txt")
