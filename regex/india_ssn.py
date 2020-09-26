#!/bin/env python
""" https://www.hackerrank.com/challenges/valid-pan-format/ """


import re
n = input()

for _ in range(int(n)):
    what = input()

    if re.match(r'[A-Z]{5}\d{4}[A-Z]', what):
        print('YES')
    else:
        print('NO')
