
# 1. find the Intersection (common elements) of two lists ?
print("find the Intersection (common elements) of two lists")
list1 = [1,2,3,4,5]
list2 = [2,3,5,6,7]

# using for loop
def intersection_loop(list1, list2):
    common_list = []
    for item in list1:
        if item in list2 and item not in common_list:
            common_list.append(item)
    return common_list 
print(intersection_loop(list1, list2))  

# using list comprehension
def intersection_comp(list1, list2):
    return [item for item in list1 if item in list2]
print(intersection_comp(list1, list2))

# 2. find the most frequent element in a list ?
print("find the most frequent element in a list")

numbers = [1, 2, 2, 3, 4, 4, 5 ,5, 4]

def most_freq(list):
    max_count = 0
    most_freq = None
    for item in list:
        count = list.count(item)
        if count>max_count:
            max_count = count
            most_freq = item
    return most_freq
print(most_freq(numbers))


# 3. find cumulative sum of a list
print("find cumulative sum of a list")

number= [1, 2, 3, 4]

def cumulative_sum(list):
    cum_sum =[]
    total = 0
    for num in list:
        total +=num
        cum_sum.append(total)
    return  cum_sum   
print(cumulative_sum(number)) 

# 4. Remove duplicstes from a list
print("Remove duplicates from a list")

fruits = ["apple", "banana", "mango", "cherry", "banana", "apple"]

# using loop 
def remove_duplicates(list):
    unique = []
    seen = set()
    for item in list:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return unique
print(remove_duplicates(fruits))

# using set constructor
print(list(set(fruits))) # set removes duplicates 

# 5. find the index of an element in a tuple
print("find the index of an element in a tuple")
my_tuple = (1, 2, 3, 4)

def find_index(tup, elem):
    return tup.index(elem) if elem in tup else -1
print(find_index(my_tuple, 3))

# 6. find the most frequent vqlue in a dictionary
print("find the most frequent vqlue in a dictionary")

data = {'a':1, 'b':2, 'c':1, 'd':3, 'e':1}

def most_frequent(dct):
    frequency = {}
    for value in dct.values():
        if value not in frequency:
            frequency[value] = 0
        frequency[value] += 1 #1:1, 2:1, 1:2, 3:1, 1:3
    max_value = max(frequency, key=frequency.get)    
    return max_value
print(most_frequent(data))