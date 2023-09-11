import random

a = ['a','b','c','d']
rand = random.choice(a)
print(rand)
rand2 = random.sample(a,2)
print(rand2)
rand3 = random.choices(a,k=4)
print(rand3)
random.shuffle(a)
print(a)

n = int(input('how many numbers in range:'))
s = int(input('from which number:'))
for i in range(n):
    random.seed(s)
    print(random.randint(s,s+200))