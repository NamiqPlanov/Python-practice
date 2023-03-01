arr  = [2,2,3,4]
target = 5
n=len(arr)
for i in range(n-1):
    for j in range(i+1,n):
        if i!=j:
           if arr[i]+arr[j] == target:
               print(arr[i],j)
