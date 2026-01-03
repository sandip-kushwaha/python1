
'''Write a Python program to create a calculator that can perform at least five
different mathematical operations such as addition, subtraction, multiplication,
division and average. Ensure that the program is user-friendly, prompting for input
and displaying the results clearly.'''

# step-1: create functions.

# function to addition two numbers
def add(num1, num2):
    return num1+num2

# function to substraction two numbers
def sub(num1, num2):
    return num1-num2

# function to multiplication two numbers
def multiply(num1, num2):
    return num1*num2

# function to divide two numbers
def divide(num1, num2):
    return num1/num2

# function to avarage two numbers
def avg(num1, num2):
    return (num1+num2)/2

# Step-2: user input

print("Please Select a operation:\n"\
      "1. Addition\n"\
      "2. Substration\n"\
        "3. Multiplication\n"\
            "4. Division\n"\
                "5. Average\n")
select = int(input("Select a operation from 1, 2, 3, 4, 5: "))

num1 = int(input("Enter the first number: "))
num2 = int (input("Enter the second number: "))


#Step-3: print the result

if select == 1:
    print(num1, "+", num2,"= ", add(num1, num2))

elif select == 2:
    print(num1, "-", num2, "= ", sub(num1, num2))  

elif select == 3:
    print(num1, "*", num2, "= ", multiply(num1, num2))

elif select == 4:
    print(num1, "/", num2, "= ", divide(num1, num2))

elif select == 5:
    print("(",num1,"+",num2,")","/", "2: ", avg(num1, num2))            

else:
    print("Invalid operaton! please Select again!")
