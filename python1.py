arr = [1,2,3,4]
n = len(arr)
target = 6
for i in range(0,n):
    for j in range(0,n):
        if arr[i]+arr[j] == target:
            print (i,j)





