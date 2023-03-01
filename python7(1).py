def commonprefix(str):
    prefix = ''
    i = -1
    while True:
        i+=1
        for word in str:
            if len(word)<i+1 or word[i]!=str[0][i]:
                return prefix
        prefix+=str[0][i]
print(commonprefix(['abc','ab','abcd']))


#time complexity is 2 because 
#if time complexity = 0(we should find(number of words*length of the shortest word))
#then,i is the lenght of the shortest word and i+1 is the number of words in array.
#then, we should multiply i(i+1)
        