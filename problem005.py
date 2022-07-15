# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest(r, s):
    n = 1
    while (n <= r):
        c = 0
        for d in range(1,s+1):
            if (n % d != 0):
                break
            else:
                if (d == s):
                    return n
        n += 1
    return -1

print("Solution: ", smallest(1000000000, 20))
