from palindrome import is_palindrome

def test_is_palindrome():
    assert is_palindrome("racecar") == True

test_is_palindrome()

def test_mixed_case():
    assert is_palindrome("Racecar") == True

test_mixed_case()

def test_spaces():
    assert is_palindrome("never odd or even") == True

test_spaces()

def test_empty():
    assert is_palindrome("") == True

test_empty()