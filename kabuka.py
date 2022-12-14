import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# %matplotlib inline

# AAPL=ティッカーシンボル
aapl = yf.Ticker('AAPL')
muzi = yf.Ticker('7453.T')
days = 20 
hist = aapl.history(period=f'{days}d')
hist_muzi = muzi.history(period=f'{days}d')
print(pd.concat([hist, hist_muzi], axis=1).head())