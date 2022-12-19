import streamlit as st
import yfinance as yf
import pandas as pd
import altair as alt

muzirushi = yf.Ticker('7453.T')
days = 20
hist = muzirushi.history(period=f'{days}d')

hist.index = hist.index.strftime('%d %B %Y')
hist = hist[['Close']]
hist.cloumns = ['無印良品']
hist.head()
hist = hist.T
hist.index.name = 'Name'
print(hist)