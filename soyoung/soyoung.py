import requests , bs4,re
def save(id):
    uid = 'u'+str(id)
    res = requests.get('http://www.soyoung.com/' + uid)
    res.raise_for_status()
    text = bs4.BeautifulSoup(res.text)
    elem = text.select('p.name a')
    try:
        name = elem[0]['title']
    except:
        return 0


    info = text.select('div.con')
    #print (info[0])

    pr = re.compile(r'<p>(.*)</p>')
    p = pr.findall(str(info[0]))
    p.insert(0, name)
    p.insert(0, uid)
    #print (p)

    heartFile = open('user.txt', 'a')
    s = "  , ".join(p)
    try:
        heartFile.write("\n" + s)
    except:
        return 0

    heartFile.close()


for i in range(271,500000) :
    save(i)