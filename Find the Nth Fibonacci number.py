"""
Function that when given a number (n),
returns the n-th number in the Fibonacci Sequence.
"""

def nth_fib(n):
    if n <= 0: # if 0 is entered as n, returns none
        return None
    elif n == 1: # returns 0 as 1st fibonacci number
        return 0
    elif n == 2: # returns 1 as 2nd fibonacci number
        return 1
    else:
        return nth_fib(n-1) + nth_fib(n-2) # the nth number is the sum of the two previous fibonacci numbers


print(nth_fib(9)) # should return 21
print(nth_fib(10)) # should return 34
print(nth_fib(4)) # should return 2
print(nth_fib(0)) # should return none