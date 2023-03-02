def Palindrome(x):
    reverse = 0
    temp = x
    while temp>0:
        reverse = (reverse*10)+(temp%10)
        temp = temp//10
    if reverse == x:
        return True
    else:
        return False

print(Palindrome(121))


