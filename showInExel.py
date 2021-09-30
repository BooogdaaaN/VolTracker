import json
import xlsxwriter
import xlrd

with open('db.txt') as json_file:
    coins = json.load(json_file)

workbook = xlsxwriter.Workbook('volumeTracker.xlsx')
worksheet = workbook.add_worksheet('sheet')
row = 0
column = 0

for i in coins:
    worksheet.write(row, 0, i['symbol'])
    worksheet.write(row, 1, float(i['volume']))
    # worksheet.write(row, 2, i['volDay2'])
    # worksheet.write(row, 3, i['volDay3'])
    row+=1    
workbook.close()

# Readme:
#     1) if you start tracking You should: comment all worsheet.write except 15-16
#     2) to continue You should: add another worksheet.write(row, 'current day number;, i['volDay(current day number)'])