#Exercises - Lists, Dictionaries, Tuples

#1. Create a list of names and print the second item.
#2. Create a list of sports and then replace the second item with another sport.
#3. Create a list containing numbers and delete the fifth number from the array.
#4. Create two lists of numbers and merge them.
#5. Create a list of numbers and find the length, minimum, and maximum.
#6. Create a dictionary of students and scores and print out a student’s score.
#7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair.
#8. Create a dictionary of names and ages and then print out all the keys and values
#9. Create a tuple of your favorite movies
#10. Create a tuple and print all the items from the first to third index.

#Exercise 1
nameList = ['John', 'Steve', 'Ana', "Kate"]
print(nameList[1])
print()

#Exercise 2
sportList = ['Soccer', 'Basketball', 'Football', 'Volleyball']
sportList[1] = 'Hockey'
print(sportList)
print()

#Exercise 3
numList = [1, 2, 6, 23, 13, 27]
del numList[4]
print(numList)
print()

#Exercise 4
numList1 = [1, 54, 12, 31, 24]
numList2 = [9, 429, 123]
print(numList2 + numList1)
print()

#Exercise 5
oddNumList = [1, 75, 131, 97, 17]
print(len(oddNumList))
print(max(oddNumList))
print(min(oddNumList))
print()

#Exercise 6
students = {'Ana': 93, 'Derrek': 82, 'Chelsea': 98, 'Draven': 100}
print(students['Chelsea'])
print()

#Exercise 7
namesAges = {'Qiyana': 19, 'Moiker': 28, 'Bob':32, 'Stevie':72, 'Josh':32}
del namesAges['Moiker']
print(namesAges)
print()

#Exercise 8
namesAges1 = {'bob':23, 'bill':11, 'Austin':23, 'betty':92}
print(namesAges1)
print()

#Exercise 9 & 10
mytup = ('Titanic', 'Shark Tales', 'Interstellar', 'Bee Movie')
print(mytup[1:4])
print()
