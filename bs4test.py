import requests , bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()
text = bs4.BeautifulSoup(res.text)

html = open('test.html')
h = bs4.BeautifulSoup(html.read())
print (h)
elems = h.select('#csszengarden')
print (elems)
