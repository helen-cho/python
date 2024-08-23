import csv
import json

data = []
with open('data/코스피시가총액1~100.csv', 'r', encoding='utf-8') as csv_file:
  reader = csv.DictReader(csv_file)
  data = list(reader)

with open('data/코스피시가총액1~100.json', 'w', encoding='utf8') as json_file:
  json_file.write(json.dumps(data, indent=4, ensure_ascii=False))