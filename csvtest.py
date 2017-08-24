import csv

file = open('example.csv')
csvReader = csv.reader(file)
data = list(csvReader)

print (data)