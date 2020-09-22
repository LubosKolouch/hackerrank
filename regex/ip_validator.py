#!/bin/env python
""" https://www.hackerrank.com/challenges/ip-address-validation/problem """
import re

n_cases = input()

for _ in range(int(n_cases)):
    what = input()
    if re.match(r'\b((?:\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}'
                r'(?:\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\b', what, flags=re.VERBOSE):
        print(f"{what} IPv4")
    elif re.match(r'\b([0-9a-f]{1,4}:){7}[0-9a-f]{1,4}\b', what):
        print(f"{what} IPv6")
    else:
        print(f"{what} Neither")
