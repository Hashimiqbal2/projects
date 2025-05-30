#What are data structures, and why are they important?
"Data structures are ways to organize and store data in a computer so"
" that it can be accessed and modified efficiently."
""
" They are important because they provide a means to manage large amounts of data, "
"allowing for efficient data retrieval, storage, and manipulation."

#) Explain the difference between mutable and immutable data types with examples
"Mutable data types can be changed after creation, while immutable data types cannot."
"Examples of mutable data types include lists and dictionaries"
"while examples of immutable data types include strings and tuples."


#3) What are the main differences between lists and tuples in Python
"Lists are mutable, meaning they can be changed after creation,"
" while tuples are immutable and cannot be changed. "
"Lists are defined using square brackets [], "
"while tuples are defined using parentheses (). "
"Lists have more built-in methods than tuples, such as append() and remove(). "
"Tuples can be used as keys in dictionaries, while lists cannot."


#4)Describe how dictionaries store data)
"Dictionaries store data in key-value pairs,"
" where each key is unique and maps to a specific value."
" They are implemented as hash tables, allowing for fast access to values based on their keys. "
"In Python, dictionaries are defined using curly braces {} or the dict() constructor, "
"and they allow for efficient data retrieval and manipulation."

#5  Why might you use a set instead of a list in Python
"A set is used instead of a list when you want to store unique elements and do not care about the order of the elements. Sets automatically handle duplicates and provide efficient membership testing, making them suitable for operations like union, intersection, and difference. In Python, sets are defined using curly braces {} or the set() constructor."
#6)P What is a string in Python, and how is it different from a list

"A string in Python is a sequence of characters enclosed in single or double quotes."
" It is immutable, meaning once created, "
"it cannot be changed. In contrast, a list is a mutable collection that can hold items of different data types and can be modified after creation. Strings are primarily used for text manipulation, while lists are used for storing collections of items."

#7) How do tuples ensure data integrity in Python?
"A tuple ensures data integrity in Python by being immutable,"
" meaning once a tuple is created, its elements cannot be changed,"
" added, or removed. "
"This immutability guarantees that the data remains constant throughout the program, preventing accidental modifications. Tuples are often used to represent fixed collections of items where the integrity of the data is crucial."

#8) What is a hash table, and how does it relate to dictionaries in Python?
"A hash table is a data structure that implements an associative array abstract data type"
", "
"a structure that can map keys to values. In Python, dictionaries are implemented using hash tables, "
"allowing for efficient key-value pair storage and retrieval. "
"Each key in a dictionary is hashed to produce a unique index, "
"enabling fast access to the corresponding value."

#9)  Can lists contain different data types in Python?
"Yes, lists in Python can contain different data types. "
"A single list can hold integers, strings, floats, and even other lists or dictionaries."
" This flexibility allows for the creation of complex data structures "
"and makes lists a versatile choice for storing collections of items."


#10)Explain why strings are immutable in Python?
"Strings are immutable in Python to ensure data integrity and performance. "
"Immutability means that once a string is created, it cannot be changed. "


#11) What advantages do dictionaries offer over lists for certain tasks?
"""
Dictionaries offer several advantages over lists for certain tasks:
1. Fast Lookup: Dictionaries provide fast access to values using unique keys, while lists require searching through elements.
2. Key-Value Pair Storage: Dictionaries store data as key-value pairs, making it easy to associate related information.
3. Uniqueness: Each key in a dictionary is unique, preventing duplicate entries for the same identifier.
4. Efficient Updates: Updating or retrieving a value by key is more efficient in dictionaries than searching by value in lists.
Dictionaries are ideal for tasks like storing user information, configuration settings, or any data that requires quick access by a unique key.
"""

#12)  Describe a scenario where using a tuple would be preferable over a list
"""
A tuple is preferable over a list when you want to store a collection of values 
that should not change throughout the program.
 For example, storing the coordinates of a point (x, y), 
 RGB color values, or the days of the week. Since tuples are immutable, 
 they help ensure that the data remains constant and cannot be accidentally modified.
"""
#13 How do sets handle duplicate values in Python?
"""
In Python, sets automatically remove duplicate values. 
When you add elements to a set, 
only unique values are stored. If you try to add a duplicate, 
it will be ignored. This property makes sets useful for storing collections of unique items.
"""
#14 How does the “in” keyword work differently for lists and dictionaries?
"""
In lists, the “in” keyword checks if a value exists among the elements of the list. 
In dictionaries, the “in” keyword checks if a value exists among the dictionary’s keys, 
not its values. 
For example, 'a' in [1, 'a', 3] returns True, 
while 'name' in {'name': 'Alice', 'age': 30} also returns True because 'name' is a key.
"""

#15 Can you modify the elements of a tuple? Explain why or why not
"""
No, you cannot modify the elements of a tuple
 because tuples are immutable in Python. 
 Once a tuple is created, its elements cannot be changed, added, or removed. 
 This immutability ensures that the data stored in a tuple remains constant throughout the 
 program.
"""

#16)What is a nested dictionary, and give an example of its use case?
"""
A nested dictionary is a dictionary where the values can also be dictionaries. This allows you to store more complex, hierarchical data structures. 

Example use case:
student = {
    "name": "Alice",
    "grades": {
        "math": 90,
        "science": 85
    },
    "address": {
        "city": "Srinagar",
        "zip": "190001"
    }
}
"""

#17) Describe the time complexity of accessing elements in a dictionary
"""
Accessing elements in a dictionary has an average time complexity of O(1),
 meaning it takes constant time regardless of the size of the dictionary. 
 This efficiency is due to the underlying hash table implementation, 
 which allows direct access to values using their keys.
"""
#18) In what situations are lists preferred over dictionaries?
"""
Lists are preferred over dictionaries when you need to maintain the order of elements, 
store items without unique identifiers, 
or perform operations that rely on element positions 
(like indexing, slicing, or sorting). Lists are ideal for storing sequences of items where the relationship between elements is based on their order rather than a key-value association.
"""
#19) Why are dictionaries considered unordered, and how does that affect data retrieval?
"""
Dictionaries are considered unordered because, before Python 3.7, 
they did not maintain the insertion order of key-value pairs. T
his means the order in which items are stored or retrieved is not guaranteed. 
As a result, you cannot rely on the order of elements when iterating over a dictionary. 
However, data retrieval by key is not affected, as you can always access values directly 
using their unique keys regardless of order.
"""

#20 Explain the difference between a list and a dictionary in terms of data retrieval.
"""
A list retrieves data by position (index), so you access elements using their numeric 
index (e.g., list[0]). A dictionary retrieves data by key,
 so you access values using unique keys (e.g., dict['name']). 
 This makes dictionaries faster and more efficient for looking up values by identifier,
   while lists are better for ordered collections where position matters.
"""



#1)Write a code to create a string with your name and print it
#str  as string to store values 
str="hashim iqbal akhoon"    #stored values inside string

print(str.title())   #printed the string in title case 



#2)Write a code to find the length of the string "Hello World"

str1="hello world"

print(len(str1))   #printed the length of string



#3) Write a code to slice the first 3 characters from the string "Python Programming
str2="python programming"
print(str2[0:3])  #printedd through positive indicies

#with negative indicies

print(len(str2)) 

print(str2[:-15])#printed the first three characters of string



# 4)Write a code to convert the string "hello" to uppercase

word="hello"
print(word.upper())  #cstring conversion/string modification



# 5)Write a code to replace the word "apple" with "orange" in the string "I like apple"
str3="I like apple"
print(str3.replace('apple','orange'))   #replace method used for repacling characters inside string

#5) Write a code to create a list with numbers 1 to 5 and print it
list=[1,2,3,4,5]   #list created with numbers
for i in list:print(list[0:5])  #printed the list with numbers  with loops 

print(list[-5:])  #with negative indicies


#6Write a code to append the number 10 to the list [1, 2, 3, 4]
list3=[1,2,3,4]  #list created with numbers
list3.append(10)  

print(list3) 


#7) Write a code to remove the number 3 from the list [1, 2, 3, 4, 5]

list=[1,2,3,4,5]
list.remove(3)    #method to remove elements

print(list)

#7)Write a code to access the second element in the list ['a', 'b', 'c', 'd']
list4=['a','b','c','d'] 
print(list4[1]) 
print(list4[-3])  
#8) Write a code to reverse the list [10, 20, 30, 40, 50].

list5=[10,20,30,40,50] 

print(list5[::-1])   #general reverse method

#9 Write a code to create a tuple with the elements 100, 200, 300 and print it.

tuple=(100,200,300)   #tuple creation
print(tuple[0:4])   #tuple printing withn indicies method


#10) Write a code to access the second-to-last element of the tuple ('red', 'green', 'blue', 'yellow').
tuplex=('red','green','blue','yellow')  #tuple creation
print(tuplex[2:3])

print(tuplex[-2])  #with negative indicies

#11) Write a code to create a tuple with the elements 100, 200, 300 and print it.
our_tuple=(100,200,300)
for elements in tuple:
    print(elements)  

#!@) Write a code to access the second-to-last element of the tuple ('red', 'green', 'blue', 'yellow')

colours=('red','green','blue','yellow')

for elm in colours:
    print(colours[:-2])
    #or
    print(colours[2:3])

#13) Write a code to find the minimum number in the tuple (10, 20, 5, 15).

tuple1=(10,20,5,15)  
print(min(tuple1))  #minimum number printed with min method

#14)4. Write a code to find the index of the element "cat" in the tuple ('dog', 'cat', 'rabbit').
tuple2=('dog','cat','rabbit') 
print (tuple2.index('cat'))  #index method used to find the index of element


#15) Write a code to create a tuple containing three different fruits and check if "kiwi" is in it.
fruit=('apple','kiwi','watrmelon')  
if 'kiwi' in fruit:
  print('available')
else:
  print('not available')

  #16)Write a code to create a set with the elements 'a', 'b', 'c' and print it.
  set={'a','b','c'}  #set created
print(set)  #set printed


#17)  Write a code to clear all elements from the set {1, 2, 3, 4, 5}.
set1={1,2,3,4,5}  
set1.clear()
print(set1)  #method/function to clear elements/sdata structure


#18)  Write a code to remove the element 4 from the set {1, 2, 3, 4}.
set2={1,2,3,4}
set2.remove(4)  
print(set2) 

#19  Write a code to find the union of two sets {1, 2, 3} and {3, 4, 5}
set3={1,2,3}
set4={3,4,5}
set5=set3.union(set4)  #union method used to find the union of two sets
print(set5)  

#20  Write a code to find the intersection of two sets {1, 2, 3} and {2, 3, 4}.
set6={1,2,3}
set7={2,3,4}
set8=set6.intersection(set7)  #intersection method
print(set8)

#21 Write a code to create a dictionary with the keys "name", "age", and "city", and print it.
dict={'name':"hashim iqbal",'age':"23",'city':"srinagar"} #dictionary created
print(dict)

#22  Write a code to add a new key-value pair "country": "USA" to the dictionary {'name': 'John', 'age': 25}
d={'name':"John",'age':"25"}  #dictionary created
d['country']='USA'  #new key value pair added   
print(d)  #dictionary printed

#24
 #Write a code to access the value associated with the key "name" in the dictionary {'name': 'Alice', 'age': 30}.
d1={'name':"Alice",'age':"30"}  #dictionary created
print(d1['name'])  #value associated with the key name printed

#25. Write a code to remove the key "age" from the dictionary {'name': 'Bob', 'age': 22, 'city': 'New York'}.
d2={'name':"Bob",'age':"22",'city':"New York"}  #dictionary created
d2.pop('age')

#26 Write a code to create a list, a tuple, and a dictionary, and print them all.
list6 = [1, 2, 3, 4, 5]  # list created
tuple3 = (10, 20, 30)  # tuple created    
dict3 = {'name': 'Alice', 'age': 30}  # dictionary created
print("List:", list6)  # list printed
print("Tuple:", tuple3)  # tuple printed
print("Dictionary:", dict3)  # dictionary printed

#27.)Write a code to create a list of 5 random numbers between 1 and 100, sort it in ascending order, and print the
list=[33,22,12,4,6]
print(list)

list.sort()
print(list)

#28) Write a code to create a list with strings and print the element at the third index.

lis=["hekko","bukko","anuu","halu"]

print(lis[3])

#29 Write a code to combine two dictionaries into one and print the result
dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}

combined_dict = {**dict_a, **dict_b}
print(combined_dict)
#30. Write a code to convert a list of strings into a set.

string_list = ["apple", "banana", "cherry", "apple"]
string_set = set(string_list)
print(string_set)