def divide(dividend,divisor):
    d = abs(dividend)
    div = abs(divisor)
    res = 0
    while d>=div:
        d-=div
        res+=1
    if (dividend<0 and divisor>=0)or(divisor<0 and dividend>=0 ):
        res = -res
    return res

print(divide(7,-3))