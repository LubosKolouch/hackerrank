import sys
import re

text = sys.stdin.read()
if re.search(r'\#include', text, re.DOTALL):
    print('C')
elif re.search(r'import\s+java', text, re.DOTALL):
    print('Java')
else:
    print('Python')
