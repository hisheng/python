import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #创建 正则表达式对象

mo = phoneNumRegex.search('my number is 415-444-5454 .') #匹配对象
print ('mo phone number found : ' + mo.group())

phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex2.search('my number is 415-444-5454 .')
print ('mo2 phone number found : ' + mo2.group())
print ('mo2 phone number found(0) : ' + mo2.group(0))
print ('mo2 phone number found(1): ' + mo2.group(1))
print ('mo2 phone number found(2): ' + mo2.group(2))


phoneNumRegex3 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') # 用?匹配0次或者1次
mo3 = phoneNumRegex3.search('My number is 555-4242')
print ('mo3 phone number found : ' + mo3.group())

batRegex = re.compile(r'Bat(wo)*man')  # 用 * 匹配0次或者多次，
mo4 = batRegex.search('The Adventures of Batman')
mo5 = batRegex.search('The Adventures of Batwoman')
mo6 = batRegex.search('The Adventures of Batwowowowowowoman')
print ('mo4 is ' + mo4.group())
print ('mo5 is ' + mo5.group())
print ('mo6 is ' + mo6.group())

#用+ 匹配 1次或者多次
#用{n} 匹配 n 次， {n,m}，匹配n到m次 比如{3,5} 匹配,3,或4 或5次

#贪心 和 非贪心匹配
greedyHaRegex = re.compile(r'(Ha){3,5}') #贪心” 的， 这表示在有二义的情况下，它们会尽可能匹配最长的字符串

mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group() # 'HaHaHaHaHa'

nongreedyHaRegex = re.compile(r'(Ha){3,5}?') #花括号的“ 非贪心” 版本匹配尽可能最短的字符串，即在结束的花括号后跟着一个问号。

mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group() #'HaHaHa

xmasRegex = re.compile(r'\d+\s\w+')
m = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print (m)


voweRegex = re.compile(r'[aeiouAEIOU]')
m1 = voweRegex.findall('RoboCop eats baby food. BABY FOOD.')
print (m1)


beginsWithHello = re.compile(r'^Hello') # ^ 开始符号  $ 结束符合
b = beginsWithHello.search('Hello world!')
print (b)
print (b.group())
bn = beginsWithHello.search('He said hello.')
print (bn)

# . 点符号 通配符合，匹配除了换行之外的 所有 单个字符