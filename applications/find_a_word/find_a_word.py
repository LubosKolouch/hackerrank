#!/bin/env python
""" Solution to the problem https://www.hackerrank.com/challenges/find-a-word/problem """

import re

n = input()

sentences = list()

for _ in range(int(n)):
    sentences.append(input())
m = input()

for _ in range(int(m)):
    count = 0
    what = input()
    for sentence in sentences:
        re_what = r'(?:[^a-zA-Z_0-9]|^|\b)'+what+'(?:[^a-zA-Z_0-9]|$)'
        finder = re.findall(re_what, sentence)
        if len(finder):
#            print(re_what)
 #           print(what)
  #          print(sentence)
   #         print(finder)
    #        print('---------------')
            count += len(finder)
    print(count)
