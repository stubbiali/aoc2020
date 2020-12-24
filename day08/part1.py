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
def execute(code, lineno, history, accumulator):
    if lineno in history or lineno > len(code):
        return accumulator
    else:
        history.add(lineno)

    line = code[lineno]

    if line[:3] == "acc":
        if line[4] == "+":
            accumulator += int(line[6:-1])
        else:
            accumulator -= int(line[6:-1])
        return execute(code, lineno + 1, history, accumulator)
    elif line[:3] == "jmp":
        if line[4] == "+":
            return execute(code, lineno + int(line[6:-1]), history, accumulator)
        else:
            return execute(code, lineno - int(line[6:-1]), history, accumulator)
    else:
        return execute(code, lineno + 1, history, accumulator)


# >>> main
def main(filename):
    with open(filename, "r") as data:
        code = list(data)
        result = execute(code, 0, set(), 0)
        print(f"The result is {result}.")


# >>> runtime
if __name__ == "__main__":
    main("input.txt")
