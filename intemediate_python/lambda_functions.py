from functools import reduce
'''
number = int(input('enter number for subtraction:'))
subtraction = lambda a:a-number
print(subtraction(20))

sum1 = lambda c,d: c+d
print(sum1(3,4))



points2D = [(1,3),(-4,7),(-3,9),(10,16)]
sorting_in_espect_with_y = sorted(points2D,key=lambda x:x[1])
sorting_in_espect_with_x = sorted(points2D,key=lambda x:x[0])
print(sorting_in_espect_with_y)
print(sorting_in_espect_with_x)
'''


list1 = [10,20,13,15,16,9,11]
list2 = map(lambda x:(x*2)+2,list1)
list3 = sorted(list2)
print(list(list2))
print(list(list3))


list4 = [a*2+2 for a in list1]
print(list4)

even_numbers = filter(lambda y:y%2==0, list1)
print(list(even_numbers))


even_numbers_for = [b for b in list(list1) if b%2==0]
print(sorted(even_numbers_for))


list6 = reduce(lambda x,y:x+y, list1)
print(list6)
