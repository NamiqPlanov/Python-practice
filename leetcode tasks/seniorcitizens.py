def seniorcitizens(info):
    ans = 0
    for line in info:
        age = int(line[11:13])
        if age>50:
            ans+=1
    return ans
print(seniorcitizens(['0554565676M34','0705431232M52']))