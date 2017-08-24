import os


print (os.path.abspath('.'))

heartFile = open('test.txt','w')
heartFile.write('hello')
heartFile.close()