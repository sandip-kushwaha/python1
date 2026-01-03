
#Create dictionary in python
# 1. Using curly braces
print("1. Using curly braces")
my_dict = {"name": "ram", "age": 25, "city": "Kathmandu"}
print(my_dict)  

# 2. Using the dict() constructor
print("2. Using the dict() constructor")
my_dict2 = dict(name="ram", age=25, city="Kathmandu")
print(my_dict2)

# Dictionary operations
print("3. Dictionary operations")
# 1. Adding elements - assign operator
my_dict3 = {"name": "ram", 
            "age": 25
            }
print("\nadd item")
my_dict3["city"] = "Kathmandu"  # Add a new key-value pair
print(my_dict3)

#modify/replace item - assign operator
print("\nmodify/replace item")
my_dict3['age'] = 20
print(my_dict3)

# 2. Removing elements del or .pop() method
print("4. Using pop() to remove an element")
my_dict4 = {"name": "ram", "age": 25, "city": "Kathmandu"}
removed_value = my_dict4.pop("age")  # Remove a key-value pair and return the value
print("Removed value:", removed_value)  
print(my_dict4)

# Using popitem() to remove the last inserted key-value pair
print("5. Using popitem() to remove the last inserted key-value pair")  
my_dict5 = {"name": "ram", "age": 25, "city": "Kathmandu"}
removed_item = my_dict5.popitem()  # Remove the last inserted key-value pair    
print("Removed item:", removed_item)
print(my_dict5)

# Using del to remove a key-value pair
print("6. Using del to remove a key-value pair")
my_dict6 = {"name": "ram", "age": 25, "city": "Kathmandu"}
del my_dict6["city"]  # Remove a key-value pair
print(my_dict6)

# Using clear() to remove all elements
print("7. Using clear() to remove all elements")
my_dict7 = {"name": "ram", "age": 25, "city": "Kathmandu"}
my_dict7.clear()  # Remove all key-value pairs
print(my_dict7)  # Output: {}

# Dictionary Methods
print("Dictionary Methods")
my_dict8 = {"name": "ram", 
            "age": 25, 
            "city": "Kathmandu"
            }
#1. keys() - Returns a view object that displays a list of all the keys in the dictionary
print("Keys:", my_dict8.keys())  # Output: dict_keys(['name', 'age', 'city'])

#2. values()- return all values
print("values:", my_dict8.values())

#3. items() - return all key-value pair
print("items:", my_dict8.items())

# 4. get() method - return value for a key
print("get:", my_dict8.get('age')) 


# Dictionary Iterations
print("\nDictionary Iterations\n")

student={
       "name":"Ram",
       "age":20,
       "grade":"A"
}
# loop through key
for key in student:
    print("key:",key)
# loop through value 
for value in student:
    print("value:", student[value])

# Using .values() method
for value in student.values():
    print(value)

# loop through both key-value pair
for keys, value in student.items():
    print(keys, value)

# Nested dictionary
print("\nNested dictionary")
students = {
    "student1":{
        "name":"Ram",
        "age": 24,
        "grade": "A"
    },
    "student2":{
        "name":"Shyam",
        "age":22,
        "grade": "B"
    }
} 
# print(students)
stu = students["student1"].keys()
print(stu)
# print(students["student1"])
# print(students["student1"]["name"])


# Dictionary Comprehension
print("\nDictionary Comprehension")
# syntax 
# new_dict={key_exp : value_exp for item in iterable if condition} 

square = {x: x * x for x in range(1, 6)}
print(square)