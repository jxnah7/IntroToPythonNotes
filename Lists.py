#Intro to lists, a series of values based on its index

shoppingList = ['Apples', 'Oranges', 'Bananas', 'Cheese'] #array format
print(shoppingList[0:3])    #prints index 0/1/2 


shoppingList.append('Apricots') #append adds to the back
print(shoppingList) #prints new list with added element 'Apricots'


shoppingList[0] = 'ApplePie' #replaces index 0 with new element ApplePie
print(shoppingList)

del shoppingList[1] #deletes the element found in index 1 which was 'Oranges'
print(shoppingList)


print(len(shoppingList)) #prints the length of the list which is 4


shoppingListTwo = ['Bread', 'Jam', 'PB'] #Declare and initialize another list holding 3 elements
print(shoppingList + shoppingListTwo) #Merged both shopping lists together
print(shoppingList * 2) #Prints the list twice

numList = [1, 4, 7, 23, 6]
print(max(numList)) #Prints the biggest number in the list
print(min(numList)) #Prints the smallest number in the list
