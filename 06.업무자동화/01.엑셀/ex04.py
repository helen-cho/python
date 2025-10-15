from openpyxl import Workbook
from random import *

wb = Workbook()
ws = wb.active

ws.append(['번호', '영어', '수학'])
for i in range(1, 11):
    ws.append([i, randint(0, 100), randint(0, 100)])

for row in ws.iter_rows(min_row=2, max_row=5):
    for col in row:
        print(col.value, end=',')
    print()

wb.save('data/sample.xlsx')
wb.close()