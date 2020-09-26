import re

my_str = ' '.join([input() for _ in range(int(input()))])

for _ in range(int(input())):
    word = input()
    am_word = re.sub('ou', 'o', word, 0)
    count = len(re.findall(word+r'\b', my_str))
    count += len(re.findall(am_word+r'\b', my_str))
    print(count)
