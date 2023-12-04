def two_sign_digits(num):
    return abs(num)>=10
def elem_with_digits(arr):
    res = [elem for elem in arr if two_sign_digits(elem)]
    return res

print(elem_with_digits([10,11,3,4,5,111]))