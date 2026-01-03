
# functions without parameters

def greeting(): #parameter
    print("Hello, How are you?")

greeting() #Argument

# function with parameters
def number(a, b):
    return a+b

sum = number(2, 4)
print("sum: ", sum)
print(type(sum))