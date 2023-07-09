list1 = [1,True,'John','acac','acve']
item = list1[:]
if len(list1)>3:
    list1.insert(2,'Ayxan')
    print(list1)
else:
    print('false')

print(type(list1))
list1.append('abcds')
print(list1)

list1.extend(['hello','bro'])
print(list1)
print(list1.index('acac'))


list2 = [123,543,234,567]
max1 = max(list2)
print(max1)
print(list2.index(max1))
print(list2.count(123))

list2.reverse()
print(list2)
list2.remove(543)
print(list2)
list2.pop(2)
print(list2)


list2.clear()
print(list2)
list2.append(['hello','abi','eqc',23])
print(list2)

list3 = list2.copy()
print(list3)
list4 = [12,1,14,5,3]
list4.sort()
print(list4)
lsitfinal = list1+list2
print(lsitfinal)
number_list = [1,2,4,5,7,8]
product_list = [i+i for i in number_list]
print(product_list)
    


        
        




