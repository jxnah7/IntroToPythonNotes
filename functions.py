# Functions

def helloWorld():
    print("Hello World!")

def greeting(name):
    print("Hi " + name + "!")
    
greeting("Jonah")


# here we simply print the result of x and y 
def simpleAddition(x, y):
    print(x + y)
simpleAddition(5, 10)


# here we save the result instead and assign it to the variable numSum
def add(num1, num2):
    return num1 + num2
    
numSum = add(5, 10)
print(numSum)

# Same thing with multiplication instead
def mult(num3, num4):
    return num3 * num4



print(mult(add(1,2), add(3,4))) # gets sum of numbers then multiplies each other
