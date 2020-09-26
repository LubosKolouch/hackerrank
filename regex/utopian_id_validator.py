#!/bin/env python
""" https://www.hackerrank.com/challenges/utopian-identification-number/ """

import re

n = input()

for _ in range(int(n)):
    my_id = input()

    if re.match(r'^[a-z]{0,3}\d{2,8}[A-Z]{3,}', my_id):
        print('VALID')
    else:
        print('INVALID')
