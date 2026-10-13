print("\nQ1a\n")
# Q1a: Replicate the following functions as lambda functions

# function

def square(n):
    return n*n

# lambda

square = lambda n: n * n

print(square(2))

# function

def percentage(n):
    return n/100

# lambda

percentage = lambda n: n / 100

print(percentage(2))

# function

def multiplier(n, m):
    return n*m

# lambda

multiplier = lambda n, m: n * m

print(multiplier(2, 5))

# function

def addition(a, b, c):
    return a + b + c

# lambda

addition = lambda a, b, c: a + b + c

print(addition(2, 3, 4))

# A1a:


print("\nQ1b\n")
# Q1b: Write an explanation of how this factorial lambda function works
factorial = lambda a: a*factorial(a-1) if (a>1) else 1

# A1b:
"""
Lambda takes a parameter (a) and keeps calling the function until it reaches 1 (e.g. if a = 5, it calculates:
5 * factorial(4)
4 * factorial(3)
3 * factorial(2)
2 * factorial(1)
factorial(1) = 1 stops calling the function because of the condition a > 1

so then:
2 * 1 = 2
3 * 2 = 6
4 * 6 = 24
5 * 24 = 120)
"""

print("\nQ1c\n")
# Q1c: Using the Map function alongside a lambda function, take the list_of_numbers
# and generate a list of all of the numbers squared
list_of_numbers = [23, 345, 45, 76, 87, 4, 2, 0]

# A1c:

squared = list(map(lambda n: n * n, list_of_numbers))

print(squared)

# -------------------------------------------------------------------------------------- #