import requests
import json

def get_jsonOf_CurCoinsVolume():
    response = requests.get("https://api2.binance.com/api/v3/ticker/24hr")
    allCoins = json.loads(response.text)
    curAllCoinsUsdt = []
    for coin in allCoins:
        if coin['symbol'][-4:]== 'USDT':
            curAllCoinsUsdt.append(coin)   
    
    for coin in curAllCoinsUsdt: 
            # del coin['symbol']
            del coin['priceChange']
            del coin['priceChangePercent']
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

curCoinsVol = get_jsonOf_CurCoinsVolume()

with open('db.txt') as json_file:
    savedCoins = json.load(json_file)
for savedCoin in savedCoins:
    for curCoin in curCoinsVol:
        if curCoin['symbol'] == savedCoin['symbol']:
            savedCoin['volDay11'] = curCoin['volume']
            # chnge     here <>
with open('db.txt', 'w') as outfile:
    json.dump(savedCoins, outfile)

# with open('db.txt', 'w') as outfile:
#     json.dump(curCoinsVol, outfile)



# README:
#     1) to start tracking You should: comment 39-46;
#     2) to continue tracking You should: uncomment 39-46; comment 48-49; in 46 change 'volDay(+1)'


