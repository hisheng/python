import json
path = 'd:/pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
open(path).readline()
records = [json.loads(line) for line in open(path)]
records[0]
records[0]['tz']

print(records[0]['tz'])