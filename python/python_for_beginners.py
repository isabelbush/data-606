# string
    # character
print(type("Isabel"))
    # escape characters
print("Isabel says \"Hi!\"")

# number
    # integer
print(type(10))
    # float
print(type(9.99))

print(5)

# boolean
    # true
print(type(True))
    # false
print(type(False))

print(2 < 4)

# variables
first_name = "Isabel"
last_name = "Bush"
age = 28
weight = 70
height = 160
    # concatenation
print(first_name + ' ' + last_name)

# operators
    # addition
x = 4
y = x + 5
z = y + x
print(z)
    # subtraction
a = 10
b = a - 2
c = a - b
print(c)
    # multiplication
d = 10
e = d * 2
f = d * e
print(f)
    # division
g = 20
h = g / 2
i = g / h
print(i)
    # modulus
j = 10
k = 3
l = 10 % 3
print(l)
    # increment
m = 3
m += 1
print(m) # m = m + 1
    # decrement
n = 3
n -= 1
print(n) # n = n - 1
    # greater than
o = 12 > 11
print(o)
    # less than
p = 11 < 12
print(p)
    # greater than or equal to
q = 10 >= 10
print(q)
    # less than or equal to
r = 13 <= 13
print(r)
    # equal to
s = "Isabel" == "Isabel"
print(s)
    # not equal to
t = "Isabel" == "Isabel"
print(t)

# lists
    # indexes
shopping_list = ["bread", "milk", "cheese"]
print(shopping_list[2])
print(shopping_list[-1])
    # append method
shopping_list.append("eggs")
print(shopping_list)
    # pop method
removed_item = shopping_list.pop(1)
print(shopping_list)
print(removed_item)

# dictionaries
    # key:value pairs
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.keys())
print(car.values())
print(car.get("model"))
    # add item
car["colour"] = "red"
print(car)
    # update method
car.update({"colour": "green"})
print(car)
    # pop method
car.pop("year")
print(car)

# control flow
    # if statements
num = 13
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    # elif keyword
age = 13
if age < 12:
    print("parental guidance")
elif age >= 12 and age <= 14:
    print("12 rating and below")
elif age >= 15 and age <= 17:
    print("15 rating and below")
else:
    print("any film")

# loops
    # while loop
counter = 0
while counter < 5:
    print(counter)
    print("Loop is running")
    counter += 1
    # for loop
customers = {
    "name": "Bob",
    "age": 45,
    "likes-bananas": True
}
for customer in customers.values():
    print(customer)

# functions
    # parameters
def double_plus_one(number):
    result = number * 2 + 1
    print(result)
double_plus_one(5)
double_plus_one(10)
    # double parameters
def full_name(first_name, last_name):
    print(first_name + ' ' + last_name)
full_name("Jane", "Doe")
full_name("Joe", "Bloggs")
    # return
def full_name(first_name, last_name):
    return first_name + ' ' + last_name
name = full_name("Jane", "Doe")
print(name)