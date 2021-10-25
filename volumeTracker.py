import requests
import json
import xlsxwriter

def get_jsonOf_CurCoinsVolume():
    response = requests.get("https://api2.binance.com/api/v3/ticker/24hr")
    allCoins = json.loads(response.text)
    curAllCoinsUsdt = []
    for coin in allCoins:
        if coin['symbol'][-4:] == 'USDT' and coin['symbol'][-8:] != 'DOWNUSDT' and coin['symbol'][-6:] != 'UPUSDT' and coin['quoteVolume'] != '0.00000000' and coin['symbol']!= 'TUSDUSDT' and coin['symbol']!= 'USDCUSDT' and coin['symbol']!= 'BUSDUSDT' and coin['symbol']!= 'USDPUSDT' and coin['symbol']!= 'EURUSDT' and coin['symbol']!= 'AUDUSDT' and coin['symbol']!= 'GBPUSDT':
            for busdCoin in allCoins:
                if coin['symbol'][:-4]+'BUSD' == busdCoin['symbol']: 
                    curAllCoinsUsdt.append(coin)   
    
    for coin in curAllCoinsUsdt: 
            # del coin['symbol']
            del coin['priceChange']
            # del coin['priceChangePercent']
            del coin['weightedAvgPrice']
            del coin['prevClosePrice']
            del coin['lastPrice']
            del coin['lastQty']
            del coin['bidPrice']
            del coin['bidQty']
            del coin['askPrice']
            del coin['askQty']
            del coin['openPrice']
            del coin['highPrice']
            del coin['lowPrice']
            del coin['volume']
            # del coin['quoteVolume']
            del coin['openTime']
            del coin['closeTime']
            del coin['firstId']
            del coin['lastId']
            del coin['count']
            coin['volume'] = coin.pop('quoteVolume') 
    return curAllCoinsUsdt               

curCoins = get_jsonOf_CurCoinsVolume()
 
with open('db.txt') as json_file:
    savedCoins = json.load(json_file)

for savedCoin in savedCoins:
    for curCoin in curCoins:
        if curCoin['symbol'] == savedCoin['symbol']:
            savedCoin['tracking1'] = savedCoin['tracking2']
            savedCoin['tracking2'] = savedCoin['tracking3']
            savedCoin['tracking3'] = savedCoin['tracking4']
            savedCoin['tracking4'] = savedCoin['tracking5']
            savedCoin['tracking5'] = savedCoin['tracking6']
            savedCoin['tracking6'] = savedCoin['tracking7']
            savedCoin['tracking7'] = savedCoin['tracking8']
            savedCoin['tracking8'] = savedCoin['tracking9']
            savedCoin['tracking9'] = savedCoin['tracking10']
            savedCoin['tracking10'] = curCoin['volume']
            savedCoin['priceChangePercent'] = curCoin['priceChangePercent']

with open('db.txt', 'w') as outfile:
    json.dump(savedCoins, outfile)

# part 2 writing into exel
with open('db.txt') as json_file:
    coins = json.load(json_file)

workbook = xlsxwriter.Workbook('volumeTracker.xlsx')
worksheet = workbook.add_worksheet('sheet')
row = 0
column = 0

for i in coins:
    worksheet.write(row, 0, i['symbol'])
    worksheet.write(row, 1, float(i['tracking1']))
    worksheet.write(row, 2, float(i['tracking2']))
    worksheet.write(row, 3, float(i['tracking3']))
    worksheet.write(row, 4, float(i['tracking4']))
    worksheet.write(row, 5, float(i['tracking5']))
    worksheet.write(row, 6, float(i['tracking6']))
    worksheet.write(row, 7, float(i['tracking7']))
    worksheet.write(row, 8, float(i['tracking8']))
    worksheet.write(row, 9, float(i['tracking9']))
    worksheet.write(row, 10, float(i['tracking10']))
    worksheet.write(row, 12, float(i['priceChangePercent']))
    row+=1 
    
workbook.close()
