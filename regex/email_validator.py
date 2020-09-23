#!/bin/env python
""" https://www.hackerrank.com/challenges/detect-the-email-addresses/problem """

import re

n = input()
emails = set()

for _ in range(int(n)):
    what = input()
    pattern = r'\b[a-zA-Z0-9._]+\@[a-zA-Z0-9._]+\.[a-zA-Z0-9._]+\b'
    x = re.findall(pattern, what)
    for email in x:
        emails.add(email)
        #print(x)

if emails:
    print(";".join(sorted(emails)))


