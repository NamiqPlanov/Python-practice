#this function for getting first string of array
def palindromic_string(arr):
    ans = []
    n = len(arr)
    for i in range(n):
        if arr[i][::-1]==arr[i][::1]:
            ans.append(arr[i])
    if ans ==[]:
        return ''
    else:
        return ans[0]
print(palindromic_string(['aba','sadcae','ghg']))

#this function if for getting all strings of array that are palindromic

def palindromic_2(arr2):
    ans = []
    n = len(arr2)
    for i in range(n):
        if arr2[i][::-1]==arr2[i][::1]:
            ans.append(arr2[i])
    return ans
print(palindromic_2(['aba','use','wow','good']))