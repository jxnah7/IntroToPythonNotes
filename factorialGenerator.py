# Exercise: Calculate the Factorial of a Number

# Instructions:

# 1. Define a function called `calculate_factorial` that takes in one parameter, `number`.
# 2. Inside the function, write code to calculate the factorial of the given number.
# 3. The factorial of a number is the product of all positive integers less than or equal to that number. For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
# 4. You can use either loops or recursion to calculate the factorial.
# 5. Return the factorial as the output of the function.



# Example:
# Here's an example of how the function should behave:
# calculate_factorial(5)
# Expected output:
# 120

def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial
    
number = 5
print(f"Factorial of {number} is: {calculate_factorial(number)}")
