# While loops and Control statements, 

# imagine a home thermostat, it has to 
# constantly check the temperature and
# raise the heat until the desired temperature 

c = 0
d = 0
e = 0

while c < 5:
    c = c + 1
    if c == 3:
        break # break is great when youve reached your desired outcome and want to break the loop
    print(c)
print()



while d < 5:
    d = d + 1
    if d == 3:
        continue # continue will let the loop continue running but skips the rest of the current iteration
    print(d) # when d == 3, this print statement will be skipped
print()


while e < 5:
    e = e + 1
    if e == 3:
        pass # sort of a 'do nothing' placeholder
    print(e)
print()
