
# 1. star pattern
n =5  # number of rows
print("1. Star pattern")
for i in range(1, n+1):  #outer loop
    for j in range(1, i+1): #inner loop
        print("*", end=" ")
    print()

# OR
print("OR")
for i in range(1, n+1):
    print("* " * i)

# 2. inverted triangle
n = 5
print("1. inverted triangle")
for i in  range(n, 0, -1):
    for j in range(1, i+1):
        print("*", end = " ")
    print()    

    # or
print("OR")    
for i in range(n, 0, -1):
     print("* " * i)


# 3. pyramid pattern
print("3. pyramid pattern")
n = 5
for i in range(1, n+1):  #loop for no. of rows
    print(' ' * (n-i), end = " ") # spaces to center the stars
    print("*" * (2 * i - 1)) # print stars