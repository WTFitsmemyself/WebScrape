import requests

url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=50&sortBy=rank&sortType=desc&" \
      "cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added," \
      "max_supply,circulating_supply,total_supply,volume,volume_7d,volume_30d,logo,ohlc&convert=USDT"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
