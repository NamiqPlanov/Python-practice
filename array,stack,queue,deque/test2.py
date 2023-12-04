def question2(arr):
    arr.sort()
    largest_3 = arr[-3:]
    second_smallest=arr[1]
    return largest_3,second_smallest
print(question2([10,12,3,4,5,6,8]))