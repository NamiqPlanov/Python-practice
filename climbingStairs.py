def climbing(n):
    one = 1
    two = 1
    for i in range(n-1):
        temp = one+two
        one = two
        two = temp
    return two
print(climbing(13))