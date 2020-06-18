#!python

from math import sqrt

def encryption(s):

    res_arr = dict()

    without_spaces = s.replace(' ','')

    cols = int(sqrt(len(without_spaces))) + 1

    if cols < sqrt(len(without_spaces)):
        cols += 1

    for x, char in enumerate(without_spaces):
        res_arr[x % cols] = res_arr.get(x % cols, '') + char

    return (' '.join(list(res_arr.values())))


print(encryption('iffactsdontfittotheorychangethefacts'))
