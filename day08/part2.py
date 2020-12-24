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
def execute(code, lineno=0, history=None, accumulator=0):
    history = history or set()

    if lineno in history or lineno == len(code):
        return lineno == len(code), accumulator
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


def change_line(code, lineno):
    assert lineno < len(code)
    old = code[lineno]
    if old[:3] == "jmp":
        code[lineno] = f"nop{old[3:]}"
        return 1
    elif old[:3] == "nop":
        code[lineno] = f"jmp{old[3:]}"
        return 1
    return 0


# >>> main
def main(filename):
    with open(filename, "r") as data:
        code = list(data)

        history = set()
        status, result = execute(code, history=history)
        if status:
            print(f"The result is {result}.")
            exit(0)

        for lineno in range(len(code)):
            if change_line(code, lineno):
                status, result = execute(code)
                if status:
                    print(f"The result is {result}.")
                    exit(0)
                change_line(code, lineno)

        raise RuntimeError("Fail.")


# >>> runtime
if __name__ == "__main__":
    main("input.txt")
