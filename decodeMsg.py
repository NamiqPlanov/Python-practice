def decode(key,msg):
    keyToActual = {' ':' '}
    currentChar = 'a'
    for c in key:
        if c not in keyToActual:
            keyToActual[c] = currentChar
            currentChar = chr(ord(currentChar)+1)
    return ''.join(keyToActual[c] for c in msg)


print(decode(key, msg))
    