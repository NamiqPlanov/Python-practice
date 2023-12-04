def separate_numbers(arr):
    even = [num for num in arr if num%2==0]
    odd = [num for num in arr if num%2!=0]

    return even+odd

print(separate_numbers([1,2,3,4,5,6,7]))