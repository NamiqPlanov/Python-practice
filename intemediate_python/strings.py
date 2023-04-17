'''
str1 = input('enter string:')
even = []
odd = []
print(str1.lower())




for i in range(len(str1)):
    if i%2==0:
        even.append(str1[i].capitalize())
        
        
    else:
        odd.append(str1[i])




print('even characters: {}'.format(even))
print('odd characters: {}'.format(odd))
if 'o' in str1:
    print(str1.find('o'))
    print(str1.count('o'))
    print(str1.replace('o', 'a'))
else:
    print('there is no such character')


print(str1.split(","))
str3 = ['n'] *4
print(str3)
str4 = '.'
for i in str3:
    str4+=i
print(str4)

str4 = ''.join(str3)
print(str4)
'''
question1  = input('what is his/her name:')
stra = 'his/her name is %s'%question1
print(stra)
question2 = int(input('how old is he/she:'))
int1 = 'he/she is %d'%question2
print(int1)





    


