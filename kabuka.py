import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# AAPL=ティッカーシンボル
# aapl = yf.Ticker('AAPL')
# muzi = yf.Ticker('7453.T')

# hist = aapl.history(period=f'{days}d')
# hist_muzi = muzi.history(period=f'{days}d')
# print(pd.concat([hist, hist_muzi], axis=1).head())

# days = 20
# # FB→METAに変更
# tickers = {
#     'apple': 'AAPL',
#     'facebook': 'META',
#     'google': 'GOOGL',
#     'microsoft': 'MSFT',
#     'muzirushi': '7453.T'
# }
# # companyの中にキーが入ってくる（apple, facebook）
# df = pd.DataFrame()
# for company in tickers.keys():
#     tkr = yf.Ticker(tickers[company])
#     hist = tkr.history(period=f'{days}d')
#     hist.index = hist.index.strftime('%d %B %Y')
#     # 終値の指定
#     hist = hist[['Close']]
#     hist.columns = [company]
#     hist = hist.T
#     hist.index.name = 'Name'
#     df = pd.concat([df, hist])

# print(df)

aapl = yf.Ticker('AAPL')
print(aapl.info.head())