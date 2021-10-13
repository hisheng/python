import pandas as pd

df = pd.read_csv('600615.csv')

total = 0
num = 0
for row in df.values:
   total += row[0]*row[1]
   num += row[1]
   print(row)

print(total)
print(num)
print(total/num)
