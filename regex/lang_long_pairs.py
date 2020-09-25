#!/bin/env python
""" https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/problem """
import re

n_locs = input()

for _ in range(int(n_locs)):
    what =input()

    locs = re.findall(r'(?:[\( ]?[+-]?)(.*?)(?:[,\) ]+)',what)

    # it's invalid if it starts with 0
    if locs[0][0] == '0' or locs[1][0] == '0':
        print('Invalid')
        continue

    # it's invalid if it ends with .
    if locs[0][-1] == '.' or locs[1][0] == '.':
        print('Invalid')
        continue

    # it's invalid over 90 or 180
    if float(locs[0]) > 90 or float(locs[1]) > 180:
        print('Invalid')
        continue


    print('Valid')
