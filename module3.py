#Q1)Write a code to reverse a string

str="hello world i am here"

print( str[::-1])

#q2)  Write a code to count the number of vowels in a string

str2="hello world i am here"
vowels="aeiou"
count=0
for i in str2:
   if i in vowels:
        count+=1
print(count) 

#q3)Write a code to check if a given string is a palindrome or not

str="hashim"         
if str==str[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

#q4)Write a code to check if two given strings are anagrams of each other

str="listen"
str2="silent"
if sorted(str)==sorted(str2):
    print("anagram")
else:
    print("not anagram")

#q5)Write a code to find all occurrences of a given substring within another string

text = "This is a simple string, and this string is simple."
substring = "simple"
count=0
for i in range(len(text)-len(substring)+1):
    if text[i:i+len(substring)]==substring:
        count+=1
print(count)

#q6) Write a code to perform basic string compression using the counts of repeated characters


str1 = "aaabbccccdaa"
compressed = ""
count = 1
for i in range(1, len(str1)):
    if str1[i] == str1[i-1]:
        count += 1
    else:
        compressed += str1[i-1] + str(count)
        count = 1
compressed += str1[-1] + str(count)  # Add the last set
print(compressed)

#q7)  Write a code to determine if a string has all unique characters
str="hsh"
if len(str)==len(set(str)):
    print("all unique") 
else:
    print("not all unique")

#q8) Write a code to convert a given string to uppercase or lowercase
str="hello"
print(str.upper())
print(str.lower())

#q9)  Write a code to count the number of words in a string
str="hello world i am here go"
count=0
for i in str:
    if i==" ":
        count+=1
print(count+1)


#q10) Write a code to concatenate two strings without using the + operator
str1="hello"
str2="world i am here"
str3="".join([str1,str2])
print(str3)

#q11)Write a code to remove all occurrences of a specific element from a list

listr=[1,2,3,4,5,1,1,1,6,7,8,1,1,1,2,3,4,5,6]
element=1
for i in listr:
    if element in listr:
        listr.remove(element)
print(listr)

#q12)  Implement a code to find the second largest number in a given list of integers

lar=[1,2,3,4,5,6,7,8,9,1,6,7,8,9,7,34,98,12,1,2]
lar=set(lar)
lar=list(lar)
lar.sort()
print(lar[-2])
for i in range(len(lar)):
    if lar[i]>lar[-1]:
        lar[i]=lar[-1]
        break
print(lar[-2])

"""Q13)Create a code to count the occurrences of each element in a list and return a dictionary with elements as
keys and their counts as values"""
listr=[1,2,3,4,5,1,1,1,6,7,8,1,1,1,2,3,4,5,6]
countdict={}
for i in listr:
    if i in countdict:
        countdict[i]+=1
    else:
        countdict[i]=1
print(countdict)


 #q14)Write a code to reverse a list in-place without using any built-in reverse functions
list1=[1,2,3,4,5,6,7,8,9,16,1,1,12,3,4,5,6]
n=len(list1)
for i in range(n//2):
    list1[i],=list1[n-i-1],
    list1[n-i-1]=list1[i]
print(list1)

"""q15) Implement a code to find and remove duplicates from a list while preserving the original order of
elements"""

list1=[1,2,3,4,5,6,7,8,9,16,1,1,12,3,4,5,6]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

#q16)Create a code to check if a given list is sorted (either in ascending or descending order) or not
list1=[1,2,3,4,5,6,7,8,9,16,1,1,12,3,4,5,6]
if list==sorted(list1) or list1==sorted(list1,reverse=True):
    print("sorted")
else:
    print("not sorted")

#q17)Write a code to merge two sorted lists into a single sorted list
list1=[1,3,5,7,9]
list2=[2,4,6,8,10]
list3=list1+list2
list3.sort()
print(list3)

#q18)Implement a code to find the intersection of two given lists
list1=[1,2,3,4,5,6,4,5,6,6,7,3,3,3,3,7,8,9]
list2=[5,6,7,8,9,9,9,9,10,11,12]

set1=set(list1) & set(list2)
intersection=list(set1)
list(intersection)
print(intersection)

#q19) Create a code to find the union of two lists without duplicates
list1=[1,2,3,4,5,6,7,8,9]
list2=[5,6,7,8,9,10,11,12]
set1=set(list1) | set(list2)
union=list(set1)
list(union)
print(union)

#q20)Write a code to shuffle a given list randomly without using any built-in shuffle functions

# TRIED BUT NOT ABLE TO DO IT

"""q21) Write a code that takes two tuples as input and returns a new tuple containing elements that are
common to both input tuples"""

x=(1,2,3,4,5,6,7,8,9)
y=(5,6,7,8,9,10,11,12)
newtuple=tuple(set(x) & set(y))
print(newtuple)


"""q22) Create a code that prompts the user to enter two sets of integers separated by commas. Then, print the
intersection of these two sets"""

set1=input("enter first set of integers separated by commas: ")
set2=input("enter second set of integers separated by commas: ")
set3=set(set1) & set(set2)
for i in set3:
    print(i)


"""q23)Write a code to concatenate two tuples. The function should take two tuples as input and return a new
tuple containing elements from both input tuples."""
tuple1=input("enter first tuple of integers separated by commas: ")

tuple2=input("enter second tuple of integers separated by commas: ")
tuple3=tuple1+tuple2

print(tuple3)

"""#q24)Develop a code that prompts the user to input two sets of strings. Then, print the elements that are
present in the first set but not in the second set"""""

set1=(input("enter first set of strings : ")) 
set2=input("enter second set of strings separated by commas: ")

set3=(set1) - (set2)
for i in set3:
    print(i)

"""#q25)Create a code that takes a tuple and two integers as input. The function should return a new tuple
containing elements from the original tuple within the specified range of indices&"""

tuple1=(1,2,3,4,5,6,7,8,9)
start=int(input("enter starting index: "))
end=int(input("enter ending index: "))
newtuple=tuple1[start:end]
print(newtuple)

"""q26)Write a code that prompts the user to input two sets of characters. Then, print the union of these two sets"""

set1=(input("enter first set of characters : "))
set2=(input("enter second set of characters : "))
set3=set(set1) | set(set2)
for i in set3:
    print(i)

"""Q27)& Develop a code that takes a tuple of integers as input. The function should return the maximum and
minimum values from the tuple using tuple unpacking"""

tuple1=(1,2,3,4,5,6,7,8,9)
maxi=max(tuple1)
mini=min(tuple1)
print("maximum is ",maxi)
print("minimum is ",mini)

"""#q28) Create a code that defines two sets of integers. Then, print the union, intersection, and difference of these
two sets
"""
set1={1,2,3,4,5,6}
set2={5,6,7,8,9,10}
set3=set1 | set2
set4=set1 & set2
set5=set1 - set2
print("union is ",set3)
print("intersection is ",set4)
print("difference is ",set5)

"""#q29)Write a code that takes a tuple and an element as input. The function should return the count of
"""
tuple1=(1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,1,2,3)
element=int(input("enter element to be counted: "))
count=tuple1.count(element) 
print("count is ",count)

"""#q30)Develop a code that prompts the user to input two sets of strings. Then, print the symmetric difference of
these two sets"""
set1=(input("enter first set of strings : "))
set2=(input("enter second set of strings : "))
set3=set(set1) ^ set(set2)
for i in set3:
    print("the  result is this",i)

"""Q31)Write a code that takes a list of words as input and returns a dictionary where the keys are unique words
and the values are the frequencies of those words in the input list&
"""
words_list=["apple","banana","orange","apple","kiwi","banana","apple"]
word_freq={}
for words in words_list:
    if words in word_freq:
        word_freq[words]+=1
    else:
        word_freq[words]=1
print(word_freq)

"""#q32) Write a code that takes two dictionaries as input and merges them into a single dictionary. If there are
common keys, the values should be added together"""
dict1={'a':100,'b':200,'c':300}
dict2={'a':300,'b':200,'d':400}
merged_dict=dict1.copy()
for key,value in dict2.items():
    if key in merged_dict:
        merged_dict[key]+=value
    else:
        merged_dict[key]=value
print(merged_dict)
"""#q33) Write a code to access a value in a nested dictionary. The function should take the dictionary and a list of
keys as input, and return the corresponding value. If any of the keys do not exist in the dictionary, the
function should return None& """
nested_dict={'a':{'b':{'c':100}}}
keys=['a','b','c']
value=nested_dict
for key in keys:
    value=value.get(key)
    if value is None:
        break
print(value)


"""q34)Write a code that takes a dictionary as input and returns a sorted version of it based on the values. You
can choose whether to sort in ascending or descending order"""

dict1={'a':3,'b':1,'c':2,'d':4}
sorted_dict= dict(sorted(dict1.items(), key=lambda item: item[1]))
print(sorted_dict)

"""Q35) Write a code that inverts a dictionary, swapping keys and values. Ensure that the inverted dictionary
correctly handles cases where multiple keys have the same value by storing the keys as a list in the
inverted dictionary"""
original_dict={'a':1,'b':2,'c':1,'d':3}
inverted_dict={}
for key,value in original_dict.items():
    if value in inverted_dict:
        inverted_dict[value].append(key)
    else:
        inverted_dict[value]=[key]
print(inverted_dict)