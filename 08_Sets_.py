
# Create set in python

# 1. Using curly braces
print("1. Using curly braces")
my_set = {1, 2, 3, 4, 5, "ram"}    
print(my_set)

# 2. Using the set() constructor
print("2. Using the set() constructor") 
my_set2 = set([1, 2, 3, 4, 5, "ram"])
print(my_set2) 

# Set operations
print("3. Set operations")
# 1.Adding elements
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")  # Add an element
print(fruits)   

# 2. Removing elements
print("4. Using remove() to remove an element")
fruit1 = {"apple", "banana", "cherry"}
fruit1.remove("banana")  # Remove an element
print(fruit1)

# using discard() to remove an element
print("5.Using discard() to remove an element")
fruit2 = {"apple", "banana", "cherry"}
fruit2.discard("cherry")  # Remove an element
print(fruit2)    

#Set Methods
print("Set Methods")

set1={1, 2, 3,6,4}
set2={3, 4, 5}
union_set=set1.union(set2) #OR  set1 | set2
print(union_set)

intersection_set = set1.intersection(set2) #OR set1 & set2
print(intersection_set)

Difference_set = set1.difference(set2) #OR set1 - set2
print(Difference_set)

symmetric_diffe_set = set1.symmetric_difference(set2) #OR set1 ^ set2
print(symmetric_diffe_set)


