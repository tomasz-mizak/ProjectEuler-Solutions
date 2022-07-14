# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from time import sleep
from tokenize import String

t = []
for a in range(900, 999):
    for b in range(900, 999):
        t.append(a*b)

# filter palindroms
_t = []
for e in t:
    s = str(e)
    if (s[0] == s[5] and s[1] == s[4] and s[2] == s[3]):
        print(s) # answer is the last console printed 's'