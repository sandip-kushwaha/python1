#create a tuple
  #1. using parentheses
print("1. using parentheses")
fruits=("apple", "banana", "cherry")
print(fruits)

#2. using without parentheses
print("2. using without parentheses")
num = 1, 2, 3, 4, 5
print(num)

# 3. using tuple() constructor
print("3. using tuple() constructor")
fruit1 = tuple(("apple", "banana", "cherry"))
print(fruit1)
# 4. using tuple() constructor with a list
print("4. using tuple() constructor with a list")
list1 = ["x", "y", "z"]
tuple1 = tuple(list1)
print(list1)
print(tuple1)

# 5. single element tuple
print("5. single element tuple")    
single_tuple = ("apple",)  # Note add comma
print(single_tuple)

#accessing tuple elements
print("6.Accessing tuple elements")
fruits = ("apple", "banana", "cherry")
print(fruits[0])  # Access first element  

#slicing a tuple
print("7.Slicing a tuple")  
fruits = ("apple", "banana", "cherry", "orange", "kiwi")
print(fruits[1:4:2])  # Access elements from index 1 to 3

#packing and unpacking tuples

print("8. packing and unpacking tuples")
a = "Ram"
b = 20
c = "student"
pack_tuple = a, b, c
print(pack_tuple)

name, age, profession = pack_tuple
print(name)
print(age)
print(profession)

# modify tuple
print("10. modify tuple")

my_tuple =("ram", "sita")
y= list(my_tuple)
y.append("shyam")
my_tuple = tuple(y)
print(my_tuple)


# Tuple Use Case - Examples

# Storing Fixed Data (Immutable Data)
# Example: Storing geographic coordinates (latitude, longitude) or RGB color values, where
# the values shouldn’t be changed after assignment

coordinate = (40.7128, -74.0060) #latitude and longitude for NYC
rgb_color = (255, 0, 0) #RGB value for red


# Using Tuples as Keys in Dictionaries
# Since tuples are immutable and hashable, they can be used as keys in dictionaries, unlike lists

location_data = {
(40.7128, -74.0060): "New York City",
(34.0522, -118.2437): "Los Angeles"
}
print(location_data[(40.7128, -74.0060)])