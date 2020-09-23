#!/bin/env python
""" https://www.hackerrank.com/challenges/detect-the-domain-name/problem?h_r=next-challenge&h_v=zen """
import re

n_lines = input()

output = set()

for _ in range(int(n_lines)):
    what = input()

    pattern = r'(?:http[s]?:\/\/(?:ww.\.)?)(.*?)(?:[\/"\?\' _\\])'
    x = re.findall(pattern, what)

    for p in x:
        if "." not in p or p in output:
            continue
        #print(f"{what} -> {p}")
        output.add(p)

print(";".join(sorted(output)))
