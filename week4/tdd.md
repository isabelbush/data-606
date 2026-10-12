# Test-Driven Development

Write a failing test before you write the code that passes the test
1. Red: write test and watch it fail
2. Green: write just enough code to pass test
3. Refactor: clean up code and tests

## Red

```python
# test_palindrome.py

from palindrome import is_palindrome

def test_is_palindrome():
    assert is_palindrome("racecar") == True
```
Returns an error because `palindrome.py` does not exist yet

## Green

```python
# palindrome.py

def is_palindrome(text):
    return text == text[::-1]
```
Test now runs successfully

## Red

```python
# test_palindrome.py

from palindrome import is_palindrome

def test_mixed_case():
    assert is_palindrome("Racecar") == True
```
Returns an error because code does not account for capital letters

## Green

```python
# palindrome.py

def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]
```
Test now runs successfully

## Red

```python
# test_palindrome.py

from palindrome import is_palindrome

def test_spaces():
    assert is_palindrome("never odd or even") == True
```
Returns an error because code does not account for spaces

## Green

```python
# palindrome.py

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]
```
Test now runs successfully

## Refactor

Add type hint
```python
# palindrome.py

def is_palindrome(text: str) -> bool:
    text = text.lower().replace(" ", "")
    return text == text[::-1]
```
Run tests again to confirm code still works