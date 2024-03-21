#Intro to dictionaries, imagine a classroom scenario where each student has a unique name and age

students = {'Bob': 12, 'Rachel': 13, 'Emily': 15} 
print(students['Rachel'])

students['Rachel'] = 14 #Happy birthday Rachel, here we update your age in our dictionary
print(students)

del students['Emily'] #Emily graduated so we delete her off the dictionary
print(students)

print(len(students))
