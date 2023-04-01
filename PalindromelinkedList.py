def Palindromelinkedlist(head: Optional[ListNode]) -> bool:
    head = current
    arr = []
    while current:
        arr.append(current.val)
        current = current.next
    for i in range(len(arr)//2):
        if arr[i]!=arr[-i-1]:
            return False
    return True

print(Palindromelinkedlist([1,2,2,1]))
