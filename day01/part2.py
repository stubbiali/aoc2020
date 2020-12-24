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
    with open(filename, "rb") as data:
        data = list(data)

        for i in range(len(data) - 2):
            it1 = int(data[i])
            for j in range(i + 1, len(data) - 1):
                it2 = int(data[j])
                for k in range(j + 1, len(data)):
                    try:
                        it3 = int(data[k])
                    except ValueError:
                        pass

                    if it1 + it2 + it3 == 2020:
                        print(f"The result is {it1 * it2 * it3}.")
                        return

        raise RuntimeError("Fail.")


# >>> runtime
if __name__ == "__main__":
    main("input.txt")
