# Python

Most popular language
- Beginner friendly
- Open source
- Multi platform
- Community
- Supporting libraries

Wide industry application
- Web
- Machine learning
- Data science
    - NumPy
    - Pandas
    - SciPy

```python
# Single-line comment
```
```python
"""
Multi-line comment
"""
```

# Data Types

## Numbers

Integer or float
```python
print(5)
print(5.50)
```
Returns `5` and `5.5`
```python
print (type(5))
print (type(5.50))
```
Returns `<class 'int'>` and `<class 'float'>`

### Operators

- `+` = add
- `-` = subtract
- `*` = multiply
- `/` = divide
- `%` = modulo
```python
print(5 * 5.50)
```
Returns `27.5`
```python
print (6 % 4)
```
Returns `2`

## Strings

Characters or text

`Can use double or single quotes`
```python
print("Hello World")
```
Returns `Hello World`
```python
print(type("Hello World"))
```
Returns `<class 'str'>`

### Unicode Characters

Python just sees a group of unicode characters rather than words
```python
print(u'\u0061')
```
Returns `a`
```python
print("Hello World"[1])
```
Returns `e` (second character because indexing starts at 0)
```python
print("Hello World"[-1])
```
Returns `d` (last character)
```python
print(len("Hello World"))
```
Returns `11` (total number of characters)

### Concatenation

Combine strings from multiple locations to create a new string
```python
first_name = 'Jane'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
print(full_name)
```
Returns `Jane Doe`

Cannot concatenate a string to an integer so must use casting (i.e. convert data type with `str()`, `int()` or `float()`)
```python
first_name = 'Jane'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
age = 25
print(full_name + ', ' + str(age))
```
Returns `Jane Doe, 25`

### Escape Characters

Apply `\` to space preceding quote
```python
text = "Isabel says \"Hello World\""
```
Returns `Isabel says "Hello World"`

### Methods

```python
first_name = 'jane'
print(first_name.capitalize)
```
Returns `Jane`
```python
first_name = 'jane'
print(first_name.upper)
```
Returns `JANE`
```python
first_name = 'jane'
print(first_name.replace('a', 'u'))
```
Returns `june`
```python
name = 'Jane Doe'
print(name.substring[5:7])
```
Returns `Doe`

## Boolean

True or false
```python
print(True)
```
Returns `True`
```python
print(type(True))
```
Returns `<class 'bool'>`

### Equality Operators

- `==` = equal to
- `!=` = not equal to
- `>` = greater than
- `<` = less than
- `>=` = greater than or equal to
- `<=` = less than or equal to

```python
print(4 == 4)
```
Returns `True`
```python
print(3 == 4)
```
Returns `False`
```python
print(3 != 4)
```
Returns `True`
```python
print(3 > 4)
```
Returns `False`

Can be used on different data types as long as they are in the same object hierarchy
```python
print(2 == len("2"))
```
Returns `False` ("2" is only 1 character)

### Truthy and Falsey

```python
print(bool(0))
```
Returns `False`
```python
print(bool(""))
```
Returns `False` (check for missing data)

Anything other than 0 is considered true
```python
print(bool(1))
```
Returns `True`

# Variables

Reserved memory location that stores data types and objects
```python
a = 4
print(a)
```
Returns `4`
```python
a = 4
b = 4.5
print(a + b)
```
Returns `8.5`

## Conventions

- Must start with letter or underscore (cannot start with number or non-alphanumeric character)
- Case-sensitive
- No spaces (use snake casing)

## Mutable

Variables can change
```python
first_name = 'Bob'
first_name = 'Kevin'
print(first_name)
```
Returns `Kevin` because `Bob` has been overwritten
```python
first_name = 'Bob'
print(first_name)
first_name = 'Kevin'
print(first_name)
```
Returns `Bob` and  `Kevin` because code runs linearly

# Control Flow

Evaluate condition to define whether it is true or false and execute code if true
```python
time_of_day = 6

if time_of_day > 5 and time_of_day < 12:
    print('Good Morning')
elif time_of_day > 12 and time_of_day < 18:
    print('Good Afternoon')
else:
    print('Good Evening')
```
Returns `Good Morning`

# Lists

Array of objects 

`Can be a mix of different data types but recommended to stick to the same one`
```python
list = [1, True, "string"]
print(list)
```
Returns `[1, True, 'string']`
```python
list = [1, True, "string"]
print(type(list))
```
Returns `<class 'list'>`

Lists are indexed-based and start at 0
```python
list = [1, True, "string"]
print(list[0])
```
Returns `1`
```python
list = [1, True, "string"]
print(list[-1])
```
Returns `string`

Use index to overwrite objects in list
```python
shopping_list = ["eggs", "bread", "cheese"]
shopping_list[-1] = "butter"
print(shopping_list)
```
Returns `['eggs', 'bread', 'butter']`

## Methods

### Append

```python
shopping_list = ["eggs", "bread", "cheese"]
shopping_list.append("butter")
print(shopping_list)
```
Returns `['eggs', 'bread', 'cheese', 'butter']`

### Pop

```python
shopping_list = ["eggs", "bread", "cheese"]
shopping_list.pop()
print(shopping_list)
```
Returns `['eggs', 'bread']` (remove last item from list)
```python
shopping_list = ["eggs", "bread", "cheese"]
shopping_list.pop(0)
print(shopping_list)
```
Returns `['bread', 'cheese']` (remove indexed item)

### Index

```python
shopping_list = ["eggs", "bread", "cheese"]
print(shopping_list.index("bread"))
```
Returns `1`

## Nested Lists

```python
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]
print(list_of_lists[1][2])
```
Returns `C`

## Set

Remove duplicates
```python
a = [1, 2, 2, 3]
s = set(a)
print(s)
```
Returns `{1, 2, 3}`

# Dictionaries

Dictionaries are based on key-value pairs

`Keys are usually string values and can store values of any data type`
```python
contact_list = {
    "Jane": "07854695321"
}
print(contact_list)
```
Returns `{'Jane': '07854695321'}`
```python
contact_list = {
    "Jane": "07854695321"
}
print(type(contact_list))
```
Retuns `<class 'dict'>`

Keys can be used like indexes in a list
```python
contact_list = {
    "Jane": "07854695321"
}
print(contact_list["Jane"])
```
Returns `07854695321`

Add new key-value pair
```python
contact_list = {
    "Jane": "07854695321"
}
contact_list["Bob"] = "07458169352"
print(contact_list)
```
Returns `{'Jane': '07854695321', 'Bob': '07458169352'}`

Update existing value
```python
contact_list = {
    "Jane": "07854695321"
    "Bob": "07458169352"
}
contact_list["Bob"] = "07135248796"
print(contact_list)
```
Returns `{'Jane': '07854695321', 'Bob': '07135248796'}`

## Methods

### Keys

```python
contact_list = {
    "Jane": "07854695321"
    "Bob": "07458169352"
}
print(contact_list.keys())
```
Returns `dict_keys(['Jane', 'Bob'])`

### Values

```python
contact_list = {
    "Jane": "07854695321"
    "Bob": "07458169352"
}
print(contact_list.values())
```
Returns `dict_keys(['07854695321', '07458169352'])`

### Pop

```python
contact_list = {
    "Jane": "07854695321"
    "Bob": "07458169352"
}
print(contact_list.pop("Jane"))
print(contact_list)
```
Returns `07854695321` (removed value) and `{'Bob': '07458169352'}`

## Nested Dictionaries

```python
contact_list = {
    "a": {
        "Jane": "07854695321"
    },
    "b": {
        "Bob": "07458169352"
    },
    "c" = {
        "Steve": "07658942175"
    }
}
print(contact_list["c"])
```
Returns `{'Steve': '07658942175'}`

```python
contact_list = {
    "a": {
        "Jane": "07854695321"
    },
    "b": {
        "Bob": "07458169352"
    },
    "c" = {
        "Steve": "07658942175"
    }
}
print(contact_list["b"]["Bob"])
```
Returns `07458169352`

# Loops

Apply actions to each object within a collection of objects

## While

Only operates as long as boolean condition is true
```python
loop_control = True

while loop_control:
    print("I am a loop")
```
Continuously returns `I am a loop`

### Increment

```python
counter = 0

while counter < 5:
    print(counter)
    counter += 1
```
Returns `0`, `1`, `2`, `3`, `4`
```python
counter = 0

while counter < 5:
    if counter % 2 == 0
        print(counter)
    else:
        print("Odd number")
    counter += 1
```
Returns `0`, `Odd number`, `2`, `Odd number`, `4`

## For

Cycle through each object within iterable

Iterable = object that stores more than one value (i.e. strings, lists and dictionaries)

`character = iterable placeholder variable`
```python
string = "test"

for character in string:
    print(character)
```
Returns `t`, `e`, `s`, `t`
```python
basket = ["eggs", "bread", "cheese"]

for basket_item in basket:
    print(basket_item)
```
Returns `eggs`, `bread`, `cheese`

### Methods

```python
customers = {
    "name": "Jane"
    "age": 22
}

for customer in customers.values():
    print(customer)
```
Returns `Jane`, `22`

### Range

Returns sequence of numbers
```python
for x in range(4):
    print(x)
```
Returns `0`, `1`, `2`, `3`

# Functions

Break code down into smaller modular chunks
- More organised
- Reusable

`Only executes when called`
```python
def print_item():
    print("example")

print_item()
```
Returns `example`

## Arguments

Pass values into the function
```python
def full_name(first_name, last_name):
    print(first_name + ' ' + last_name)

full_name("Bob", "Bloggs")
```
Retuns `Bob Bloggs`

## Return

```python
def full_name(first_name, last_name):
    return first_name + ' ' + last_name

print(full_name("Bob", "Bloggs"))
```
Retuns `Bob Bloggs`

## Nested Functions

`Use print_name function to print returned values from full_name function`
```python
def full_name(first_name, last_name):
    return first_name + ' ' + last_name

def print_name(full_name_return):
    print(full_name_return)

print_name(full_name("Bob", "Bloggs"))