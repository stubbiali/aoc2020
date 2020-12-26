
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
#include <iostream>
#include <iterator>
#include <tuple>

#include "utils.hpp"

using namespace std;

void import_data(const string &filename, int max_delta, set<int> &jolts) {
    jolts.clear();

    set<int> tmp;
    ifstream data(filename);
    int a;
    while (data >> a) {
        tmp.insert(a);
    }

    auto it = tmp.begin();
    int i = 0;
    while (i < 114) {
        jolts.insert(*it);
        it++;
        i++;
    }

    jolts.insert(0);
    jolts.insert(*(prev(jolts.end())) + max_delta);
}

int get_arrangements(int max_delta, set<int>::const_iterator begin,
                     set<int>::const_iterator end) {
    if (begin == end) {
        return 0;
    }

    if (next(begin) == end) {
        return 1;
    }

    auto a = *begin;
    auto it = next(begin);
    int count = 0;

    while (it != end and (*it - a <= max_delta)) {
        count += get_arrangements(max_delta, it++, end);
    }

    return count;
}