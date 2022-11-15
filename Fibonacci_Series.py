"""
The function 'fibonacci' should return an array of fibonacci numbers.
The function takes a number as an argument to decide how many no. of elements to produce.
If the argument is less than or equal to 0 then return empty array.
"""


def fibonacci(n):
    n1, n2 = 0, 1 # numbers at the beginning of the sequence
    sequence = [] # empty list to hold the fibonacci numbers
    for n in range(n): # for loop specifies numbers in range to n
        sequence.append(n1) # add prior number to each consecutive
        n1, n2 = n2, n1 + n2 # updates the sequence rule
    if n < 0: # if n is less than 0, return empty list
        return []
    elif n < 0 and n < 1: # if n is 1/ return 1st element
        return '0' # '[0]' (Not NONE)/ quotes make '0' Truthy
    elif n >= 1 and n < 2: # if n is 2
        return sequence[0:2] # return sequence upto 2 elements
    else:
        return sequence # otherwise return sequence as normal

print(fibonacci(10)) # should return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print(fibonacci(1)) # should return [0]

print(fibonacci(4)) # should return  [0,1,1,2]

print(fibonacci(-1)) # should return []

print(fibonacci(2)) # should return [0,1]

