from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = '나의시트'

wb.save('data/sample.xlsx')
wb.close()