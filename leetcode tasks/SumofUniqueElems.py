def SumOfUniqueElements(nums):
    answer = []
    for i in nums:
        if nums.count(i)==1:
            answer.append(i)
    return sum(answer)
print(SumOfUniqueElements([1,1,1,2,2,3]))