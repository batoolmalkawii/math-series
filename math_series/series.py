"""
Fibonacci: in this function, a sequence is generated based on the summation of the first two numbers, which are 0 and 1. 
It is implemented using recursion with 2 base cases, 0 and 1.
"""
def  fibonacci(n):
    if type(n) != int:
        return ("Invalid Input")
    if n < 0:
        return ("Invalid Input")
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


"""
Lucas: in this function, a sequence is generated based on the summation of the first two numbers, which are 2 and 1. 
It is implemented using recursion with 2 base cases, 2 and 1.
"""
def  lucas(n):
    if type(n) != int:
        return ("Invalid Input")
    if n < 0:
        return ("Invalid Input")
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


"""
sum_series: in this function, a sequence is generated based on the summation of the first two numbers, which are by default 0 and 1 (fibonacci implementation).
If the first two numbers are 2 and 1, Lucas is implemented. 
Else, a sequence is generated based on the two numbers inputted by the user.
"""
def sum_series(n, first=0, second=1):
    if first == 0 and second == 1:
        return(fibonacci(n))
    if first == 2 and second == 1:
        return(lucas(n))
    else:
        if type(n) != int:
            return ("Invalid Input")
        if n == 0:
            return first
        if n == 1:
            return second
        else:
            return sum_series(n-1, first, second) + sum_series(n-2, first, second)



