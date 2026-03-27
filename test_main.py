import pytest
from main import factorial, is_palindrome

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_positive():
    assert factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

def test_palindrome_simple():
    assert is_palindrome("madam") == True

def test_not_palindrome():
    assert is_palindrome("hello") == False

def test_palindrome_phrase():
    assert is_palindrome("never odd or even") == True