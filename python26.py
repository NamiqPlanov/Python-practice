def countJewels(J,S):
    count = 0
    for item in J:
        for elem in S:
            if item ==elem:
                count+=1
    return count

print(countJewels(J='hello', S='aaz'))