
# Nested Statements:-

num=int(input("Enter the number: "))

if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("And the number is Even.")
    else:
        print("And the number is Odd.")
elif num == 0:
    print("The number is Zero.")
else:
    print("The number is Negative.")                    