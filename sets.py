#set
set={1,2,3,4,5}
print(set)

#add
set.add(6)
print(set)
#pop
set.pop()
print(set)
#remove
set.remove(3)
#discard
set.discard(1)
#usecases
set2={1,2,3,4,5,6,(7,8,9)} #allowed
print(set2)
print(len(set2))

#oprations
set3={4,5,6,7,8,9}
#union
set4=set | set3
print(set4)
#intersection
set5=set & set3
print(set5)
#difference
set6=set - set3
print(set6)
#symmetric difference
set7=set ^ set3
print(set7)

