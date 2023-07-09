def ReverseString(s):
    reverse = [word[::-1]for word in s.split()]
    return " ".join(reverse)

print(ReverseString("Hello bro"))