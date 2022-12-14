# import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# %matplotlib inline

# AAPL=ティッカーシンボル
aapl = yf.Ticker('AAPL')
days = 20 
hist = aapl.history(period=f'{days}d')
print(hist)