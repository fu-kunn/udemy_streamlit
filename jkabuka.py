import streamlit as st
import yfinance as yf
import pandas as pd
import altair as alt

st.title('株価可視化アプリ')

days = 20
tickers = {
    'muzirushi': '7453.T',
    'rakuten': '4755.T',
    'sandora': '9989.T',
    'toyota': '7203.T',
}

# def get_data(days, tickers):
df = pd.DataFrame()
for company in tickers.keys():
    tkr = yf.Ticker(tickers[company])
    hist = tkr.history(period=f'{days}d')
    hist.index = hist.index.strftime('%d %B %Y')
    hist = hist[['Close']]
    hist.columns = [company]
    hist = hist.T
    hist.index.name = 'Name'
    df = pd.concat([df, hist])
    # return df

# get_data(days, tickers)

companies = ['rakuten', 'muzirushi']
data = df.loc[companies]
data.sort_index()
data = data.T.reset_index()
data = pd.melt(data, id_vars=['Date']).rename(
    columns={'value': 'Stock Prices'}
)
chart = (
    alt.Chart(data)
    .mark_line(opacity=0.8)
    .encode(
        x="Date:T",
        y=alt.Y("Stock Prices:Q", stack=None),
        color='Name:N'
    )
)
st.write(data)
st.altair_chart(chart, use_container_width=True)