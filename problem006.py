# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

from tkinter import S


def square_root(n):
    return n*n

def sum_of_the_squares(n1,n2,s):
    if (n1 <= n2):
        s += square_root(n1)
        return sum_of_the_squares(n1+1, n2, s)
    else:
        return s

def square_of_the_sum(n1,n2,s):
    if (n1 <= n2):
        return square_of_the_sum(n1+1, n2, s+n1)
    else:
        return square_root(s)

difference = square_of_the_sum(1,100,0) - sum_of_the_squares(1,100,0)        

print("Solution: ", difference)