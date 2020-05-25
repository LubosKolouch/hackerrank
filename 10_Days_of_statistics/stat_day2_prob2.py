#!/usr/bin/env python
""" https://www.hackerrank.com/challenges/s10-mcq-1/problem """


from itertools import product
from fractions import Fraction

p = product('123456',repeat=2)


total = 0
ok = 0

for x in p:
    total += 1
    if sum(list(map(int,x))) == 6 and x[0] != x[1]:
        ok += 1


print(Fraction(ok,total))
