# Write a code to reverse a string

s="Hello, World!"

print(s[::-1])


#2)Write a code to count the number of vowels in a string
r=" i am good at nothing but still trying"

for i in r:
    if i in 'aeiouAEIOU':
        print(i, end=' ')   

    else:
        continue
print("\n")  # Print a newline for better readability    


#3Write a code to check if a given string is a palindrome or not
def  paladrome(s):
    s=s.lower()
    if s==s[::-1]:
        return True
    
    else:
        return False    
s = "madam"
if paladrome(s):    
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")

    #4Write a code to check if two given strings are anagrams of each other
def anagram(str1,str2):
     
    str1=str1.lower()
    str2=str2.lower()
    if sorted(str1) == sorted(str2):
        
        return True
        
    else:
         return False
str1 = "listen"
str2 = "silent"

if anagram(str1, str2):
    print(f"{str1} and {str2} are anagrams")
else:
    print(f"{str1} and {str2} are not anagrams")

#5) Write a code to find all occurrences of a given substring within another string?
string = "Hello, Hi, Hello"
substring = "walla"

for i in string.split(','):
    if substring in i:
      print("substring {} found in string".format(substring))
    else:
        print("substring {} not found in string".format(substring))

#6)Write a code to perform basic string compression using the counts of repeated characters



#7) Write a code to determine if a string has all unique characters?
def unique(s):
     s=s.lower()
     if len(s)== len(set(s)):
          return True   
     else:

       return False

s = "abcdefg"
if unique(s):
  print("s has unique characters")
else:
    print("s has  not unique characters")

#8)Write a code to convert a given string to uppercase or lowercase
str= "i am doing my job"

def upper(str):
    return str.upper()
def lower(str):
    return str.lower()
print("Uppercase:", upper(str))
print("Lowercase:", lower(str))

#9)Write a code to count the number of words in a string?

str1= "Hello, how are you doing today?"
str2= str1.split(',')

str3=str1.split('o')


def coun(str):
    str=str2
    len(str)

    return len(str) 
print("Number of words in the string:", coun(str))

def cou2(str):  
    str=str3
    len(str)

    return len(str)
print("Number of words in the string:", cou2(str))


#10) Write a code to concatenate two strings without using the + operator
stx="hello"
str="seige"
x=stx.join(str)
print(x)

#11 Write a code to remove all occurrences of a specific element from a list
x= [1,2,3,4,5,6,7,1,1,1,1,1]
y=1
  print("my world")
while i in x:
    print(x.remove(y))
  
    


    
    








