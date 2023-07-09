def sortbyparity(arr):
    arr.sort(key=lambda x:x%2)
    return arr
print(sortbyparity(sorted([2,3,14,4,11,10])))


#2nd answer

def sort2(arr):
    ans = sorted([])
    for num in arr:
        if num%2==0:
            ans.insert(0,num)
        else:
            ans.append(num)
    return ans
print(sort2(sorted([1,2,3,4,5])))