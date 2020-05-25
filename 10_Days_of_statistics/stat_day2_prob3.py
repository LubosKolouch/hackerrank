#!/usr/bin/env python
""" https://www.hackerrank.com/challenges/s10-mcq-1/problem """


from itertools import product
from fractions import Fraction

p = product('RRRRBBB', 'RRRRRBBBB', 'RRRRBBBB', repeat=1)

total = 0
ok = 0

for x in p:
    if x.count('R') == 2:
        ok += 1
    total += 1


print(Fraction(ok, total))
