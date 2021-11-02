import requests
import json
import sys
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

sure = input('Are you sure you want to start tracking? (to remove old DataBase and write down new one enter "Y":   ')

if sure == 'Y':
    curCoins = get_jsonOf_CurCoinsVolume()
    for coin in curCoins:
        coin['tracking1'] = coin['volume']
        coin['tracking2'] = coin['volume']
        coin['tracking3'] = coin['volume']
        coin['tracking4'] = coin['volume']
        coin['tracking5'] = coin['volume']
        coin['tracking6'] = coin['volume']
        coin['tracking7'] = coin['volume']
        coin['tracking8'] = coin['volume']
        coin['tracking9'] = coin['volume']
        coin['tracking10'] = coin['volume']
        del coin['volume']

    with open('db.txt', 'w') as outfile:
        json.dump(curCoins, outfile)
else:
    sys.exit('to continue tracking click voltracer.exe')

    

    

