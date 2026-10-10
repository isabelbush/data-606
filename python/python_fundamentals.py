# Calculator

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

choice = int(input('\n Enter 1 for addition and 2 for subtraction: '))

num1 = int(input('\n Input your first number: '))

num2 = int(input('\n Input your second number: '))

if choice == 1:
    print(num1, '+', num2, '=', add(num1, num2))
elif choice ==2:
    print(num1, '-', num2, '=', subtract(num1, num2))
else:
    print('Invalid choice')

# Scrabble calculator

one_point_letters = ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"]
two_point_letters = ["d", "g"]
three_point_letters = ["b", "c", "m", "p"]
four_point_letters = ["f", "h", "v", "w", "y"]
five_point_letters = ["k"]
eight_point_letters = ["j", "x"]
ten_point_letters = ["q", "z"]

def scrabble_calc(word):
    word_score = 0

    for letter in word:
        if letter in one_point_letters:
            word_score += 1
        elif letter in two_point_letters:
            word_score += 2
        elif letter in three_point_letters:
            word_score += 3
        elif letter in four_point_letters:
            word_score += 4
        elif letter in five_point_letters:
            word_score += 5
        elif letter in eight_point_letters:
            word_score += 8
        else:
            word_score += 10

    return word_score

print(scrabble_calc('hello'))