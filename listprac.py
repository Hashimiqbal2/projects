st=[1,2,3,6,'hashim',7.5]
print(st)
x=st.append(9)
print(st)
z=st.insert(1,'pw')
print(st)
#extend
Y=[8,9,10]
st.extend(Y)
print(st)
#CONCANATE
st1=[11,12,13]
st2=st+st1
print(st2)
#TECHINIQUES
LISTO=['h','a','s','h','i','m',1,1,1,1,12,3,4,4,5]

#index
print(LISTO.index('s'))
#count
print(LISTO.count('h'))
#len
print(len(LISTO))

#removing

#remove
print(LISTO.remove(1))
#del
del LISTO[0]
print(LISTO)

#clear
print(LISTO.clear())
#pop
print(st.pop())
print(st)
list1=[1,2,3,4,5,6]
list2=[7,8,9,10]*3
list3=list1+list2
print(list3)

#