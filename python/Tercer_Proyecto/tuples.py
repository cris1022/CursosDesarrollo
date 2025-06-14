#Son muy parecidos en las listas pero son inmutables 
mi_tuple=(1,2,3,4,5,(6,7,8,9),10,1,1,3,3)

print(type(mi_tuple))

print(mi_tuple[5][3])

print (len(mi_tuple))
print(mi_tuple.count(1))
print(mi_tuple.index(3))