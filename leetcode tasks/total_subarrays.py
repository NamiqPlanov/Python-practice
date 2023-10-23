def subarrays(arr):
    n = len(arr)
    s = len(set(arr))
    right = 0
    left = 0
    count = 0
    counter = Counter()
    while right<n:
        counter[nums[right]]+=1
        if len(counter)==s:
            counter[nums[left]]-=1
            if counter[nums[left]]==0:
                del counter[nums[left]]
            left+=1
            count+=n-right
        right+=1
    return count
print(subarrays([1,2,3,4,5]))

    