#!/bin/env python
""" https://www.hackerrank.com/challenges/stack-exchange-scraper/problem """

import sys
import re
text = sys.stdin.read()

res = re.findall(r'<h3>.*?questions\/(\d+).*?link\"\>(.*?)\<.*?relativetime\"\>(.*?)\<', text, re.DOTALL)

for item in res:
    print(";".join(item))
