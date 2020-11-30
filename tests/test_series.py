from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

###############################################################

"""
*Fibonacci* test cases:
    1. 0 -> 0
    2. 1 -> 1
    3. 9 -> 34
    4. -1 -> "Invalid Input"
    5. "a" -> "Invalid Input"
"""

def test_fib_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib_nine():
    actual = fibonacci(9)
    expected = 34
    assert actual == expected

def test_fib_minusOne():
    actual = fibonacci(-1)
    expected = "Invalid Input"
    assert actual == expected

def test_fib_a():
    actual = fibonacci("a")
    expected = "Invalid Input"
    assert actual == expected

###############################################################

"""
*Lucas* test cases:
    1. 0 -> 2
    2. 1 -> 1
    3. 7 -> 29
    4. -2 -> "Invalid Input"
    5. "b" -> "Invalid Input"
"""

def test_luc_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_luc_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_fib_seven():
    actual = lucas(7)
    expected = 29
    assert actual == expected

def test_fib_minusTwo():
    actual = lucas(-2)
    expected = "Invalid Input"
    assert actual == expected

def test_luc_b():
    actual = lucas("b")
    expected = "Invalid Input"
    assert actual == expected

###############################################################
"""
*sum_series* test cases:
    1. 9 -> 34
    2. 7, 2, 1 -> 29
    3. 4, 4, 4 -> 20
    4. 3, -2, -3 -> -8
    5. "b", 20, 25 -> "Invalid Input"
"""

def test_sum_nine():
    actual = sum_series(9)
    expected = 34
    assert actual == expected

def test_sum_seven_luc():
    actual = sum_series(7, 2, 1)
    expected = 29
    assert actual == expected

def test_sum_four():
    actual = sum_series(4, 4, 4)
    expected = 20
    assert actual == expected

def test_sum_three_minus():
    actual = sum_series(3, -2, -3)
    expected = -8
    assert actual == expected

def test_sum_b():
    actual = sum_series("b", 20, 25)
    expected = "Invalid Input"
    assert actual == expected



