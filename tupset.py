#tuple
tup=(1,2,3,5,'hashim',7.5)
print(tup)

#tup inside tuple
tup1=(1,2,3,4,(5,6),(7,8,9))
print(tup1[4][0])

tup3=(tup1+tup)
print(tup3)
print(tup3.count(1))
print(tup3.index(7.5))
print(len(tup3))
print(min(tup3[0:4]))

#list inside tuple
tupx=(1,2,3,4,[5,6,7,8])
print(tupx[4][2])

#append
tupx[4].append(9)
print(tupx)

#insert
tupx[4].insert(7,10)
print(tupx.count(1))


