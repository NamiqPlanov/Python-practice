def flipinvert(img):
    n = len(img)
    for i in range(n):
        img[i]=img[i][::-1]
    for i in range(n):
        for j in range(n[i]):
            img[i][j]^=1
    return img
