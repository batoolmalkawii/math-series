Lab2 PR: https://github.com/batoolmalkawii/math-series/pull/1

This project includes three functions: 

* **Fibonacci:** in this function, a sequence is generated based on the summation of the first two numbers, which are 0 and 1. 
It is implemented using recursion with 2 base cases, 0 and 1.

* **Lucas:** in this function, a sequence is generated based on the summation of the first two numbers, which are 2 and 1. 
It is implemented using recursion with 2 base cases, 2 and 1.

* **sum_series:** in this function, a sequence is generated based on the summation of the first two numbers, which are by default 0 and 1 (fibonacci implementation).
If the first two numbers are 2 and 1, Lucas is implemented. 
Else, a sequence is generated based on the two numbers inputted by the user.


***Note:*** the project includes User Acceptance Tests, with the following test cases: 

*Fibonacci* test cases:

    1. 0 -> 0

    2. 1 -> 1

    3. 9 -> 34

    4. -1 -> "Invalid Input"

    5. "a" -> "Invalid Input"

*Lucas* test cases:

    1. 0 -> 2

    2. 1 -> 1

    3. 7 -> 29

    4. -2 -> "Invalid Input"

    5. "b" -> "Invalid Input"

*sum_series* test cases:

    1. 9 -> 34

    2. 7, 2, 1 -> 29

    3. 4, 4, 4 -> 20

    4. 3, -2, -3 -> -8
    
    5. "b", 20, 25 -> "Invalid Input"

