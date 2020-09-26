#!/bin/env python
""" https://www.hackerrank.com/challenges/find-hackerrank/problem """

import re

n = input()

results = {0: -1, 10: 1, 1: 2, 11: 0}

for _ in range(int(n)):
    line = input()

    points = 0
    if re.search(r'^hackerrank', line):
        points += 10

    if re.search(r'hackerrank$', line):
        points += 1

    print(results[points])
