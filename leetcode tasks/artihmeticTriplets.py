def arithmeticTriplets(arr,difference):
    answer = 0
    for a in arr:
        if a-difference in arr and a+difference in arr:
            answer+=1
        
    return answer
print(arithmeticTriplets([1,2,3,4,5,6,7], 2))

def allTriplets(arr2,n):
    a = []
    for i in range(0,n-1):
        for j in range(i+1,n):
            diff = arr2[j]-arr2[i]
            if arr2[i]-diff in arr2:
                print('{}{}{}'.format((arr2[i]-diff),arr2[i],arr2[j]),end ='\n')
    a.append(arr2[i])
    return a

print(allTriplets([1,2,3,4,5,6,7,8], 2))

