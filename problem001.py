# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

r = 1000 # range
sum = 0

for n in range(r):
    if (n == 0): continue
    if (n % 3 == 0 or n % 5 == 0):
        sum += n

print("Solution: ", sum)