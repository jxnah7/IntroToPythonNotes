"""
Exercises: Variables, Operators, Strings

1. Write a script that adds 15 and 30 and divides the sum by 2. Print out the answer.

2. Initialize two variables and use arithmetic operators to add, subtract, multiply, divide, and find the remainder.

3. Create a variable called name and store your name in it as a string.

4. Create three variables in one line and assign each one a different food item.

5. Print out "Hello" ten times using arithmetic operators.

6. Set your name and age variables in one line with multiple assignment

7. Create two strings and then create a third variable combining both of the two original strings.

8. Create a string and print the fourth letter of the word.

9. Create a string and print the letters from index 0 to 5.

10. Create a variable and print all the letters from the first index until the end.
"""
#Exercise 1
x = 15
y = 30
z = x / y

print(f"The sum of 15 and 30 is {x+y}, divided by 2 is {z}")
#or
print((15+30) / 2)


#Exercise 2
a = 5
b = 10

print(f"{a + b}")
print(f"{a - b}")
print(f"{a / b}")
print(f"{a * b}")
print(f"{a % b}")

#Exercise 3
name = "Jonah"

#Exercise 4
item0, item1, item2 = "apple", "banana", "vodka"
print(f"{item0}, {item1}, {item2}")

#Exercise 5
print(" Hello " * 10)

#Exercise 6
name1, age1 = "Victor", 10
print(f"His name is {name1} and he is {age1}")

#Exercise 7
combo = "This is the first string" + " " + "and the second string."
print(combo)
#or
sen1 = "This is the first string"
sen2 = "and the second string."
print(sen1 + " " + sen2)

#Exercise 8
str0 = "Meow"
print(str0[3])

#Exercise 9
str1 = "Pythonian Lingo"
print(str1[0:6])

#Exercise 10
sen3 = "Day one of learning python after knowing c++. Today we have nice weather."
print(sen3[0: ])

