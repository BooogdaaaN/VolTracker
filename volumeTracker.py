import requests
import json

def get_jsonOf_CurCoinsVolume():
    response = requests.get("https://api2.binance.com/api/v3/ticker/24hr")
    allCoins = json.loads(response.text)
    curAllCoinsUsdt = []
    for coin in allCoins:
        if coin['symbol'][-4:] == 'USDT' and coin['symbol'][-8:] != 'DOWNUSDT' and coin['symbol'][-6:] != 'UPUSDT' and coin['quoteVolume'] != '0.00000000' and coin['symbol']!= 'TUSDUSDT' and coin['symbol']!= 'USDCUSDT' and coin['symbol']!= 'BUSDUSDT' and coin['symbol']!= 'USDPUSDT' and coin['symbol']!= 'EURUSDT' and coin['symbol']!= 'AUDUSDT' and coin['symbol']!= 'GBPUSDT' and coin['symbol']!= 'PAXGUSDT' and coin['symbol']!= 'VTHOUSDT':
            for busdCoin in allCoins:
                if coin['symbol'][:-4]+'BUSD' == busdCoin['symbol'] and busdCoin['priceChange'] != '0.00000000': 
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

suitCoins =[]
for coin in coins:
    for tracking in coin:
        if tracking == "tracking4":
            prevTracking = float(coin[tracking])
            
        elif tracking == "tracking5":
            if float(coin[tracking])<prevTracking:
                prevTracking = float(coin[tracking])
            else:
                break
        elif tracking == "tracking6":
            if float(coin[tracking])<prevTracking:
                prevTracking = float(coin[tracking])
            else:
                break
        elif tracking == "tracking7":
            if float(coin[tracking])<prevTracking:
                prevTracking = float(coin[tracking])
            else:
                break
        elif tracking == "tracking8":
            if float(coin[tracking])<prevTracking:
                prevTracking = float(coin[tracking])
            else:
                break
        elif tracking == "tracking9":
            prevTracking = float(coin[tracking])

        elif tracking == "tracking10":
            if float(coin[tracking])>prevTracking:
                suitCoins.append(coin)
            else:
                break

for coin in suitCoins:
    coin['priceChangePercent'] = float(coin['priceChangePercent'])
suitCoins.sort(key=lambda coin: coin['priceChangePercent'])
for coin in suitCoins:
    print(coin['symbol'])
