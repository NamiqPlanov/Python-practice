import sys
tuple1 = tuple([1,2,3,4,5,1,2])
print(tuple1)
for i in tuple1:
    if i==0 or i%2==0 :
        print(tuple1[i])
tuple2 = set(tuple1)
print(tuple2)
print(tuple1.count(2))
print(tuple1.index(5))

player = 'Emil','Balayev','GK'
first_name,last_name,position = player
print('{},{},{}'.format(first_name,last_name,position))


list1 = list([1,2,3,4,5,6,7])
list2 = tuple([1,2,3,4,5,6,7])
print(sys.getsizeof(list1),'bytes')
print(sys.getsizeof(list2),'bytes')









