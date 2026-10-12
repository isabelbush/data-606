"""
def is_palindrome(text):
    return text == text[::-1]
"""
"""
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]
"""
def is_palindrome(text: str) -> bool:
    text = text.lower().replace(" ", "")
    return text == text[::-1]