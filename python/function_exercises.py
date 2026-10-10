print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

print("Enter a number: ")
number = int(input())

def divisor_calc(first_number):
    divisor_list = []
    for num in range(1, first_number):
        if first_number % num == 0:
            divisor_list.append(num)
    return divisor_list

print(divisor_calc(number))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

print("Enter another number: ")
number_2 = int(input())

def factor_calc(second_number):
    is_factor = True
    if second_number not in divisor_calc(number):
        is_factor = False
    return is_factor

print(factor_calc(number_2))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:

print("Enter a letter: ")
string_letter = input()
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]

def alphabet_position(string_input):
    string_input = string_input.lower()
    return alphabet.index(string_input)

print(alphabet_position(string_letter))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

print("Enter your name: ")
name = input()

def id_number(name_input):
    name_input = name_input.lower()
    result = ""
    for letter in name_input:
        result = result + str(alphabet.index(letter))
    return result

print(id_number(name))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def password(index_string):
    total = 0
    for number in index_string:
        number = int(number)
        total = total + number

    return int(index_string) - total

print(password(id_number(name)))

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:

print("Enter a number: ")
number_3 = int(input())

def prime_function(number_input):
    divisor = 2
    is_prime = True
    while divisor < number_input:
        prime_calc = number_input % divisor
        if prime_calc == 0:
            is_prime = False
        divisor += 1
    return is_prime

print(prime_function(number_3))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

print("Enter a number: ")
number_4 = input()

def prime_function(number_input):
    while not number_input.isdigit():
        print("Please enter numbers only. Try again: ")
        number_input = input()
    else:
        number_input = int(number_input)
    divisor = 2
    is_prime = True
    while divisor < number_input:
        prime_calc = number_input % divisor
        if prime_calc == 0:
            is_prime = False
        divisor += 1
    return is_prime

print(prime_function(number_4))

# -------------------------------------------------------------------------------------- #