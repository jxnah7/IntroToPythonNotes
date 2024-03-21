# For loops, great for iterating over data structures, printing/modyfing/extracting info


list1 = ['bananas', 'apples', 'cherries']
tup1 = (2, 6, 10)

for item in list1:
    print(item)
print()

for item in tup1:
    print(item)
print()

for i in range(0, 10): # within the range of 0-9 it will print each number
    print(i)
print()

for i in range(5, 51, 5): # the 5 is the increment factor, added to current num to get next num 
    print(i)
print()    
    
    
for i in range(0, 5): # numbers 0-4 get multiplied by numbers 0-2  0 * 0, 0 * 1, 0 * 2
    for j in range(0, 3):
        print(i * j)
