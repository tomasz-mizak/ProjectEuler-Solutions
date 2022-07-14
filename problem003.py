# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

p = []

i = 2
s = 50

while (i <= s):
    p.append(i)
    i+=1

def ero(p, i):
    _p = []
    for n in p:
        if (n % i != 0):
            _p.append(n)
    return _p

ero(p,p[0])
print(p)