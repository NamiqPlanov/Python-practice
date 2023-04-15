import sys
tuple1 = ("Baki","Namiq","Ayxan")
list1 = ['Baki','Namiq','Ayxan']
print(sys.getsizeof(tuple1),'bytes')
print(sys.getsizeof(list1),'bytes')

'''
print(tuple1)

for i in tuple1:
    print(i)

if 'Bak' in tuple1:
    print('yes')
else:
    raise Exception('no!')

    
list1 = list(tuple1)
print(list1 )

city,name,brother = tuple1
print(city)
print(name)
print(brother)


tuple2 = [1,2,3,4,5,6]
a1,*a2,a3 = tuple2
print(a2)
print(a3)
print(a1)'''

import timeit
print(timeit.timeit(stmt="[1,2,3,4]",number=10))
print(timeit.timeit(stmt="(1,2,3,4)",number=10))









