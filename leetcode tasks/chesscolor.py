def chesscolor(s):
    if s[0] =='a' or s[0]=='c' or s[0]=='e' or c[0]=='g':
        if int(s[1])%2==0:
            return 'white'
        else:
            return 'black'
    else:
        if int(s[1])%2==0:
            return 'black'
        else:
            return 'white'
print(chesscolor('a2'))