# Object Oriented Programming

class Person:
    def __init__(self, name, age): # special phrase __init__ that is used as a constructor method for a class, this sets up your classes attributes
        self.name = name
        self.age = age
        
    def getName(self): # This is a method that returns the name attribute of the Person object. It takes self as a parameter, which is a reference to the current object
        return self.name
        
    def getAge(self): # Similar to getName that instead gets the age attribute
        return self.age

p1 = Person("Bob", 22) # this is our object using the class as a blueprint, p1 is our object with name and age assigned
p2 = Person("Chelsea", 18)

print(p1.getName()) # this uses the getName function for our object p1 and prints "Bob"
print(p1.getAge()) # this uses the getAge function for our object p1 and prints "22"

print(p2.getName())
print(p2.getAge())
