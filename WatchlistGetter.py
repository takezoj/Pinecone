# python trading bot
import bs4
import requests
from bs4 import BeautifulSoup

#url = 'https://finance.yahoo.com/gainers'
ONEMIL = 1000000

# Return watchlist of top 5 stocks from given URL list with volume above given threshold.
def findWatchlist(url, volumeThreshold):

    watchList = []

    r = requests.get(url, timeout=5)
    soup = BeautifulSoup(r.content, 'html5lib')

    stockList = soup.find('tbody')

    for row in stockList.findAll('tr'):

        ticker = row.a['href'].split('=')[-1]
        volString = (row.find('td', {'aria-label': 'Volume'}).text.replace(',', ''))
        volume = stringToIntConverter(volString)

        if volume >= volumeThreshold:
            watchList.append(ticker)
            if len(watchList) >= 5:
                break

    print(watchList)

# Convert Yahoo Finance formatted number strings to floats
def stringToIntConverter(num):
    if num[-1] == 'M':
        num = float(num[:-1]) * ONEMIL
    else:
        num = float(num.replace(',', ''))

    return num


findWatchlist('https://finance.yahoo.com/gainers', 100000)
