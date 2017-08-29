def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    big = bigger(a,b)
    bigger2 = bigger(big,c)
    if bigger2 == c :
        return big
    else :
        if big == a :
            return bigger(b,c)
        else :
            return bigger(a,c)






print(median(1,2,3))
