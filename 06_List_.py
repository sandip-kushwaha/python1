
# List slicing
print("List slicing")
list = [1, 2, 3, 4, 5]
print(list[0:4:3]) 
print(list[::-1])

# modifying list
  #changing an elements
print("1.changing an elements")
list1=["apple", "banana", 3, "cherry"]
list1[2] = "orange"  # change the element at index 2 to "orange"
print(list1)

  # adding an element
print("2.adding an element")
fruits= ["apple",3 , "banana",5]
fruits.append("organge")  # append "organge" to the end of the list
print(fruits)

  # remove an element
print("3.remove an element") 
fruits1= ["apple",3 , "banana",5]
fruits1.remove(5)
print(fruits1)

 # insert an element
print("4.Insert an element")
list2 = ["ram", "shyam", "radha"]
list2.insert(2, "gita")  # insert "gita" at index 2
print(list2) 

 # extend an element
print("5.Extend an element")
list1 = [1, 2, "shyam", 3]
list2 = ["ram", "sita"]
list1.extend(list2) # extend list1 with elements from list2
print(list1)

 # Clear an element
print("6.Clear an element")
list3 = [1, 2, "shyam", 3]
list3.clear() # empty list
print(list3)

 # Finding index
print("7. Finding index")
list4 = [1, "Ram", "sita", 5,"gita"]
index = list4.index("sita") # Find the index of "sita"
print(index)

 # Finding index within a range
print("8. Finding index within a range")
list5 = [1, "Ram", 2, "sita", 5,"gita"] 
index = list5.index ("gita", 3)  # Find the index of "gita" starting from index 3
print(index)

 # Reverse list
print("9. reverse list")
list6 = [1, "Ram", 2, "sita", 5,"gita"] 
list6.reverse() 
print(list6)

 # Sorting list 
print("10. Sorting list ascending and descending order")
numbers = [40, 30,10, 20, 50, 60]
numbers.sort() #default sort ascending order
print(numbers)

numbers.sort(reverse=True) #sorting list in descending order
print(numbers)
 # sorting list with strings
print("11. Sorting list with strings")
list7 = ["cherry", "apple", "mango", "banana"]
list7.sort() 
print(list7) 

 # sorting list with a key
print("12. Sorting list with a key")
list8 = ["cherry", "apple", "banana", "mango"]
list8.sort(key=len) #sort based on length of string
print(list8)

print("13. Sorting in reverse order with a key")
list8.sort(key=len, reverse=True)
print(list8)

 # pop an element
print("14. Pop an element")
numbers = [10, 20, 30, 40, 50]
popped = numbers.pop(3) #pop the element aat index 3
print(popped)  # Output: 40

#copying a list
print("15. Copying a list")
list9 = ["apple", "banana", "mango"]
copy_fruits = list9.copy()  # Create a shallow copy of the list
print(copy_fruits)  # Output: ['apple', 'banana', 'mango']

copy_fruits.append("orange")  # Modify the copied list
print(copy_fruits)  # Output: ['apple', 'banana', 'mango', 'orange']
print(list9)  # Original list remains unchanged: ['apple', 'banana', 'mango']

# Counting elements in a list
print("16. Counting elements in a list")  
list10 = [1, 2, 3, 2, 4, 2]
count_of_twos = list10.count(2)  # Count occurrences of 2
print(count_of_twos)  # Output: 3


# Join lists
print("--- Join lists ---")

list11 = [1, 2, 3]
list12 = [4, 5, 6]  

# Using the + operator to join lists
print("1. Using the + operator")     
Final_list = list11 + list12
print(Final_list)  # Output: [1, 2, 3, 4, 5, 6]

# Using the append() method to join lists
print("2. Using the append() method")
list13 = [1, 2,]
list14 = [4, 5, "a"]  
for item in list14:
  list13.append(item)  # Append each item from list13 to list14
print(list13)  # Output: [1, 2, 4, 5, 'a']


# Using the extend() method to join lists
print("2. Using the extend() method") 
list11.extend(list12)  # Extend list13 with elements from list12
print(list11)  # Output: [1, 2, 3, 4, 5, 6]


#list Comprehension
print("--- List Comprehension ---")

#create a list of squares
print("1. Create a list of squares 1 to 5")
squares = [x**2 for x in range(1,6)]
print(squares)

#filtering even numbers
print("2. Filtering even numbers from 1 to 10")
n = [m for m in range(1,10) if m % 2 == 0]
print(n)  # Output: [2, 4, 6, 8, 10]


#create a list in uppercase
print("3. Create a list in uppercase")
fruits = ["apple", "banana", "cherry"]
uppercase = [ list.upper() for list in fruits]
print(uppercase)  # Output: ['APPLE', 'BANANA', 'CHERRY']

#flatten a nested list
print("4. Flatten a nested list")

nested_list = [[1, 2, 3], [4, 5], [6]]
flatten_list = [item for sublist in nested_list for item in sublist]
print(flatten_list)  # Output: [1, 2, 3, 4, 5, 6]
