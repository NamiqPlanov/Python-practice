def absDifference(arr,target):
    asnwer = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if abs(arr[i]-arr[j]) ==target:
                answer+=1
    return answer

print(absDifference([1,2,3,4,5], 2))