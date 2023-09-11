import sys

'''def generator1():
    yield 'Namiq'
    yield 'Ayxan'

a = generator1()
for i in a:
    print(i)

def generator2(num):
    input('starting...:')
    while num>0:
        yield num
        num -=1
cd = generator2(5)
value = next(cd)
print(value)
print(next(cd))



def numbers(n):
    nums = []
    num = 0
    while num<n:
        nums.append(num)
        num+=1
    return nums

def numbers_generator(n):
    num = 0
    while num<n:
        yield num
        num+=1
print(sum(numbers_generator(5)))

print(sum(numbers(5)))

print(sys.getsizeof(numbers(5)),'kb')
print(sys.getsizeof(numbers_generator(5)),'kb')


def fibonacci(limit):
    a,b = 0,1
    while a<limit:
        yield a
        a,b = b,a+b
fb = fibonacci(8)
for i in fb:
    print(i)
'''
mygenerator = (i for i in range(18) if i%2==0)
print(sys.getsizeof(mygenerator))
mylist = [i for i in range(18) if i%2==0]
print(sys.getsizeof(mylist))