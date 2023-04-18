def goostriplets(arr,a,b,c):
    n = len(arr)
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k]):
                    ans+=1
    return ans
print(goostriplets([1,2,3,4,5,6,7,8,9], 9, 6, 5))