arr = [1,2,3,11,5,6,7,8,9]
max1 = max(arr)
print(max1)



def num_largest(arr):
    larg=small = arr[0]
    for i in arr:
        if i>larg:
            larg = i
    return larg

print(num_largest([1,2,3,4,11,15,12]))
