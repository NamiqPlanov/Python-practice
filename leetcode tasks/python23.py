


def perm(nums):
    n = len(nums)
    ans = []
    for i in range(n):

      val = nums[nums[i]]
      ans.append(val)
    return ans
print(perm([4,5,6,2]))



