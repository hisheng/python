def big(x,y):
    if x > y :
        return x
    return y

def biggest(x,y,z):
    max = big(x,y)
    return big(max,z)


print (biggest(3,1,2))