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
    worksheet.write(row, 2, float(i['volDay2']))
    worksheet.write(row, 3, float(i['volDay3']))
    worksheet.write(row, 4, float(i['volDay4']))
    worksheet.write(row, 5, float(i['volDay5']))
    worksheet.write(row, 6, float(i['volDay6']))
    worksheet.write(row, 7, float(i['volDay7']))
    worksheet.write(row, 8, float(i['volDay8']))
    worksheet.write(row, 9, float(i['volDay9']))
    #addAndchange here   <>     and here  <>
    row+=1 
workbook.close()

# Readme:
#     1) if you start tracking You should: comment all worsheet.write except 15-16
#     2) to continue You should: add another worksheet.write(row, 'current day number;, i['volDay(current day number)'])