
# 1. factorial number
print("1. Factorial number")
def factorial(n):
    result = 1
    while n > 0:
        result *= n   # 5*1, 5*4, 20*3, 60*2, 120
        n -= 1
    return result
print(factorial(5))   

# 2. Count vowels in a string
print("2. Count vowels in a string")

my_string = "Hello, i am sandip"
vowels = "aeiou"
count = 0

for char in my_string:
    if char.lower() in vowels:
        count += 1
print("Number of vowels are:", count)        

# 3. Longest word in a string

print("3. longest word in a string")
sentence = "Hello, i am sandip kushwaha"
words = sentence.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word is:", longest_word)


# 4. Fibonacci sequence

print("4. Fibonacci sequence.")

def fibonacci(n):
     a,b = 0,1 
     count = 0
     while count < n:
         print(a, end = " ")
         a,b = b, a+b
         count += 1
fibonacci(8)
# 5. do-while loop in python 

print("\n5. do-while loop")
while True:
    num = int(input("Enter a number greater than 10: "))

    if num > 10:
        print(f"Valid number entered: {num}")
        break #exit the loop when condition is satisfied.
    else:
        print("Number is not greater than 10, Please try again !!! ")

      