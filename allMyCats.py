catName = []

while True :
    print ('input cat name')
    name = input()
    if name == '' :
        break
    catName = catName + [name]

print ('cats')

for name in catName :
    print (name)