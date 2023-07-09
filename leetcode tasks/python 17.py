def duplicate(arr):
    n = len(arr)
    for i in range(n):
        for j in (arr[:i]+arr[i+1:]):
            if 2*arr[i]==j:
                return True
        return False