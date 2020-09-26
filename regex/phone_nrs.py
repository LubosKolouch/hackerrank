import re

n = input()

for _ in range(int(n)):
    what = input()

    nr = re.findall(r'(\d+)[- ](\d+)[- ](\d+)', what)

    print(f'CountryCode={nr[0][0]},LocalAreaCode={nr[0][1]},Number={nr[0][2]}')
