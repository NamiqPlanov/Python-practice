

try:
    name = input('enter your fullname for creating email:')
    email = '@gmail.com'
    if len(name)>9:
        print(name+email)
    else:
        print('')
except:
    print('not valid name')

    