import functools

'''def starting_task(func):
    
    def wrapper():
        print('hello')
        func()
        print('goodbye')
    return wrapper

@starting_task
def fullname():
    full = input('enter fullname:')
    print(fullname)
fullname()
'''
'''def abc(func):
    def wrapper2(*args,**kvargs):
        print('hello')
        func(*args,**kvargs)
        print('goodbye')
    return wrapper2
@abc
def start_task():
    print('Namiq')

start_task()
'''

'''def start_task2(func):
     
    @functools.wraps(func)
    def wrapping(*args,**kvargs):
        print('start task')
        result = func(*args,**kvargs)
        print('end task')
        return result
    return wrapping

@start_task2
def task2():
    num = int(input('enter number'))
    return num+21

print(help(task2))
print(task2.__name__)
'''

def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapping(*args,**kwargs):
            for _ in range(times):
                res = func(*args,**kwargs)
            return res
        return wrapping
    return decorator
n = int(input('how many times:'))
@repeat(times=n)
def st():
    print('Namiq Ayxan')
st()



