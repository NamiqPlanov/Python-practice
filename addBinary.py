def addBinary(a,b):
    result = ""
    carry = 0
    a = a[::-1]
    b = b[::-1]
    n = len(a)
    m = len(b)
    for i in range(max(n,m)):
        digitsA = ord(a[i]) - ord('0') if i<n else 0
        digitsB = ord(b[i]) - ord('0') if i <m else 0
        total = digitsA + digitsB + carry
        char = str(total%2)
        result = char + result
        carry = total//2
    if carry:
        result = '1'+result
    return result

print(addBinary('11', '1'))

