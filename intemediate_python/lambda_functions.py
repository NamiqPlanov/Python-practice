''' from functools import reduce
minus_10 = lambda a:a-10
print(minus_10(15))

def minus_5(a):
    return a-10
print(minus_5(3))

multiple_nmbers = lambda c,d:c*d
print(multiple_nmbers(2,3))

coordinates = [(1,2),(-2,4),(12,15)]
sorted_coordinates = sorted(coordinates)
sorted_y = sorted(coordinates,key=lambda x:x[1])
print(sorted_coordinates)
print(sorted_y)

arr = [10,12,13,1,4,11]
mult = map(lambda a:a*2,arr)
print(list(mult))
mult2 = [e*2 for e in arr]
print(mult2)

arr2 = [12,13,14,15,17,18]
even = filter(lambda f:f%2==0,arr2)
print(list(even))

even2 = [g for g in arr2 if g%2==0]
print(even2) 

k = [1,2,3,4,5,6]
product = reduce(lambda x,y:x*y,k)
print(product)
'''
sum1 = lambda x,y:x+y
print(sum1(3,4))

coordinates = [(1,2,3),(5,-6,-2),(11,23,14),(12,13,0)]
sorted1 = sorted(coordinates,key=lambda a:a[2])
print(list(sorted1))

arr = [1,2,3,4,5,6]
arr_map = map(lambda b:b*2-3,arr)
print(list(arr_map))