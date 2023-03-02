def commonprefix(str):
   
    smallest = float('inf')
    for word in str:
      smallest = min(smallest,len(word))
      
    prefix = ''
    for i in range (smallest):
        currentchar = str[0][i]
        for word in str:
            if word[i]!=currentchar:
                return prefix
        prefix += currentchar
    return prefix

print(commonprefix([]))






# it is not constant for space complexity because the prefix is dependent on the  shortest word in string array!
#it is linear for time complexity because of prefixes. as much prefixes there are, as much the solutions

