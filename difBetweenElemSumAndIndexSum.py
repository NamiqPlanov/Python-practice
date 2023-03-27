def elemsumdigitsum(arr):
    x = y = 0
    for i in arr:
        x+=i
        n = i
        while n!=0:
            y+=n%10
            n//=10
    return abs(x-y)
print(elemsumdigitsum([10,20,21,22]))
