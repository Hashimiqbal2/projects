#dic is unorderd collection,unique and works on key pairs
#keys ca be string, listtuple but not set
#values can be anything
dic={"named":"hashim",'age':24,'city':"karachi"}
print(dic)
dic["named"]="ali" #update value
print(dic)

# list
d={"skills":"football,""cricket"}
print(d)
print(d["skills"][0])


#modification
dix={"named":"hashim",'age':24,'city':"kashmir"}
print(dix.pop("age"))
print(dix)
#del
del dix["city"]
print(dix)
d.get("named")  # returns value of key named
print(dix)
print(dix.keys()) #returns all keys
print(dix.values()) #returns all values

dic.fromkeys((1,2,3),("hashim","ali","hussain")) #creates dictionary with each key having same value
#dictionary comprehension
students=["hashim","ali","hussain"]
marks=[ 90,80,70]
for i in zip(students,marks):
    print(i)

#without making first
students={"student_marks:{}"}
for students,marks  in zip(students,marks):
    students_marks[students]=marks
    print(students_marks)