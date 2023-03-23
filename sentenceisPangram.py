def pangram(sentence:str)->bool:
    return len(set(sentence))==26

print(pangram('qwertyuiopasdfghjklzxcvbnn'))