#!/bin/env python
""" https://www.hackerrank.com/challenges/ide-identifying-comments/problem """

import fileinput
import re

output = ''
in_comment = 0

for line in fileinput.input():
    pattern = r'(\/\/.*)'
    x = re.findall(pattern, line)
    if x:
        output += x[0]
        output += "\n"
    
    if in_comment or re.search(r'\/\*', line):
        in_comment = 1

    if in_comment:
        output += re.findall(r'(?:\s*)(.*)', line)[0]
        output += "\n"

    if re.search(r'\*\/', line):
        in_comment = 0

print(output)
