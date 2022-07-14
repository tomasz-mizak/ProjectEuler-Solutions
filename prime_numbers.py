import math

def ero(p, k):
    i = p[k]
    _p = []
    for n in p:
        if (n == i):
            _p.append(n)
        else:
            if (n % i != 0):
                _p.append(n)
    if (i < math.sqrt(_p[len(_p)-1])):
        return ero(_p, k+1)
    return _p

def get_prime_numbers(n):
    primals = []
    i = 2
    s = n
    # append numbers to specified scope in n parameter
    while (i <= s):
        primals.append(i)
        i += 1
    return ero(primals, 0)