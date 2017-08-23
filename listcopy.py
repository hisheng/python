# python 的 列表 赋值 为 引用

full = ['zhang','hisheng']

zhanghisheng = full
zhanghisheng[0] = 'zh'

#此时
print (zhanghisheng,full) # ['zh', 'hisheng'] ['zh', 'hisheng']


#如果要复制的话
import copy
name = copy.copy(zhanghisheng)
name[0] = 'z'
print (name,zhanghisheng,full) # ['z', 'hisheng'] ['zh', 'hisheng'] ['zh', 'hisheng']