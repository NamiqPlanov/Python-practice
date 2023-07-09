'''a = [1,2,3,4,5]
sum1 = 0
n = len(a)
for i in range(n):
    sum1+=i
print(sum1)

print(min(a))
'''
'''
a = ['hello','zdbz','dzbzdfbs','3564']
ans = 0
for i in a:
    if len(a)>1 and i[0]==i[-1]:
        ans+=1
print(ans)
'''
'''
a = [1,2,3,4,5,6,1,2,3]
dup = set()
unique = []
for i in a:
    if i  not in dup:
        unique.append(i)
        dup.add(i)
print(dup)
'''
'''
str1 = 'i will got to party tomorrow'
new_str = str1.split(" ")
new_arr = []
n = int(input('enter number of the minimum length of string:'))
for a in (new_str):
    if len(a)<n:
        print('not valid number')
        break
for i in new_str:
    if len(i)>n:
        new_arr.append(i)
print(new_arr)
'''
'''
l1 = [1,2,3,4,5]
l2 = [5,4,6,7,2]
ans = False
count = 0
for a in l1:
    for b in l2:
        if a==b:
            ans =True
            count+=1
if ans:
    print('there are {} common number in two lists'.format(count))
else:
    print('there are no common number in two lists')
'''