import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(res.text[:250])


test = requests.get('http://localhost/python/test.txt')
print (test.text)