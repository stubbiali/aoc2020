
// -*- coding: utf-8 -*-
//
// Advent of Code 2020
//
// Copyright (C) 2020, Stefano Ubbiali
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
#include <fstream>
#include <iterator>

#include "utils.hpp"

using namespace std;

void import_data(const string &filename, set<int> &jolts) {
    jolts.clear();

    ifstream data(filename);
    int a;
    while (data >> a) {
        jolts.insert(a);
    }
}

int get_diff_counts(const set<int> &jolts) {
    if (jolts.empty()) {
        return 0;
    }

    auto first = jolts.cbegin();
    auto last = jolts.cend();

    int d1 = (*first == 1);
    int d3 = 1;

    for (auto it = first; it != last; ++it) {
        auto a = *it;
        auto b = *next(it);
        if (b - a == 1) {
            d1++;
        } else if (b - a == 3) {
            d3++;
        }
    }

    return d1 * d3;
}