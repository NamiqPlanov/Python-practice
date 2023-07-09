def seperate(arr):
    str1 = ''
    for num in arr:
        str1+=str(num)
    str1 = list(str1)
    ans = []
    for num in str1:
        ans.append(int(num))
    return ans
print(seperate([15,23,57]))