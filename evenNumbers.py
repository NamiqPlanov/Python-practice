def even(arr):
    ans=0
    for i in arr:
        if len(str(arr))%2==0:
            ans+=1
    return ans
print(even([10,12,13,14,15]))


#2nd solution

def even2(arr):
    return len([num for num in arr if len(str(num))%2==0])
print(even2([10,11]))