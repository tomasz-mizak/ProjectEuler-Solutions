# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import prime_numbers

scope = 100000 # specify scope for primals
primes = prime_numbers.get_prime_numbers(scope)

n = 600851475143

print("loaded primes: ", len(primes))
for d in primes:
    if (n % d == 0):
        print("found factor: ", d) # last factor is answer