import requests

URL = 'https://api.coinone.co.kr/ticker?currency=all'
response = requests.get(URL).json()

coinone_btc = float(response['btc']['last'])
coinone_xrp = float(response['xrp']['last'])
coinone_eos = float(response['eos']['last'])
coinone_bat = float(response['bat']['last'])

# def numberWithCommas(x):
#   return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
# }
print(coinone_btc)