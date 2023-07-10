str1 = '   hello bro'
str2 = 'good'
str3 = str1+' '+str2
print(str3)
print(str1)
str11 = str1.strip()
print(str11)
for i in str1:
    if str1[i]%2==0:
        print(str1[i].upper())