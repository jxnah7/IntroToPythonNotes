#Intro to tuples, tuples are immutable, or in other words cannot be modified

tup = ('oranges', 'apples', 'bananas')
print(tup)

# tup[0] = 'cherries' will give error since we are not allowed to modify a tuple

print(tup[0:2]) #we can still slice them

tup1 = (12, 14)
tup2 = tup + tup1 #we can still concatenate tuples

print(tup2)
