import csv

columnName = ['day', 'all', 'login', 'sku', 'order', 'pay']

users = [
    [20171013, 10000, 1000, 100, 10, 1],
    [20171012, 20000, 2000, 200, 20, 2],
    [20171011, 30000, 3000, 300, 30, 3]
]

f = open('order.csv', 'w')
csvf = csv.writer(f)

print('file name is - ' + f.name)

csvf.writerow(columnName)
csvf.writerows(users)

f.close()
