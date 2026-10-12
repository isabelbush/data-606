# Object-Oriented Programming

Group related data and functionality into objects
- Class = blueprint that defines object by:
    - State = what it has (properties or attributes)
    - Behaviour = what it does (functions or methods)
- Object = individual instance created from class
    - `__init__()` = initialise an object
    - `self` = current object
    - `name` = value
    - `self.name` = attribute that stores that value on the object
- Method = function within a class
```python
# dog.py

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(self.name + " barked")
```
Assign values to attributes to create objects
```python
dog1 = Dog("Luna")
dog2 = Dog("Lassie")
```
Access attributes using dot notation
```python
print(dog1.name)
print(dog2.name)
```
Returns `Luna` and `Lassie`

Call methods
```python
dog1.bark()
dog2.bark()
```
Returns `Luna barked` and `Lassie barked`

## Abstraction

Hide implementation details from user

```python
# main.py

from dog import Dog

dog1 = Dog("Luna")
dog2 = Dog("Lassie")

dog1.bark()
dog2.bark()
```
Returns `Luna barked` and `Lassie barked` without the user seeing the method

## Inheritance

Subclass objects inherit properties and methods from superclass

```python
# guide_dog.py

from dog import Dog

class GuideDog(Dog):
    def __init__(self, name):
        super().__init__(name)
        self.is_guide_dog = True
    
    def guide(self):
        print(self.name + " guides")
```
Call methods from both the subclass and the superclass
```python
# main.py

from guide_dog import GuideDog

dog3 = GuideDog("Lily")

dog3.guide()
dog3.bark()
```
Returns `Lily guides` and `Lily barked` even though the `bark()` method is defined in the Dog class

## Encapsulation

Control how data is accessed and modified
- Double underscore before attribute stores it privately
- `@property` = read private attribute like a normal attribute
- `@age.setter` = change an attribute with optional validation
```python
# dog.py

class Dog:
    def __init__(self, name):
        self.name = name
        self.__age = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value
    
    def bark(self):
        print(self.name + " barked")
```
Access and modify attribute via the `@property`
```python
# main.py

from dog import Dog

dog1 = Dog("Luna")

dog1.age = 5
print(dog1.age)
```
Returns `5`
```python
dog1.age = -2
print(dog1.age)
```
Still returns `5` because the `@age.setter` condition has not been met

## Polymorphism

Different objects respond to same method in different ways
```python
# dog.py

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(self.name + " barked")

    def move(self):
        print(self.name + " runs freely")
```
Define new `move()` function in subclass that overrides the `move()` function inherited from the superclass
```python
# guide_dog.py

from dog import Dog

class GuideDog(Dog):
    def __init__(self, name):
        super().__init__(name)
        self.is_guide_dog = True
    
    def guide(self):
        print(self.name + " guides")

    def move(self):
        print(self.name + " walks beside its owner")
```
Call the same method on different objects
```python
# main.py

from dog import Dog
from guide_dog import GuideDog

dog2 = Dog("Lassie")
dog3 = GuideDog("Lily")

dog2.move()
dog3.move()
```
Returns `Lassie runs freely` and `Lily walks beside its owner` even though the same method is called