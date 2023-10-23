def work_hours(hours:list[int],target):
    ans = 0
    for i in hours:
        if i >=target:
            ans+=1
    return ans
print(work_hours([1,2,3,4],2))