# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import prime_numbers

primes = prime_numbers.get_prime_numbers(1000000)

i = 1
while(i<len(primes)-1):
    print(i, "st] = ", primes[i-1])
    if (i == 10001): break
    i += 1