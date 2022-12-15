import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import altair as alt

# AAPL=ティッカーシンボル
# aapl = yf.Ticker('AAPL')
# muzi = yf.Ticker('7453.T')

# hist = aapl.history(period=f'{days}d')
# hist_muzi = muzi.history(period=f'{days}d')
# print(pd.concat([hist, hist_muzi], axis=1).head())

days = 20
# FB→METAに変更
tickers = {
    'facebook': 'META',
    'apple': 'AAPL',
    'google': 'GOOGL',
    'microsoft': 'MSFT',
    'muzirushi': '7453.T'
}
# companyの中にキーが入ってくる（apple, facebook）
df = pd.DataFrame()
for company in tickers.keys():
    tkr = yf.Ticker(tickers[company])
    hist = tkr.history(period=f'{days}d')
    hist.index = hist.index.strftime('%d %B %Y')
    # 終値の指定
    hist = hist[['Close']]
    hist.columns = [company]
    hist = hist.T
    hist.index.name = 'Name'
    df = pd.concat([df, hist])

_="""
locは行名と列名で位置を指定、ilocは行番号と列番号で位置を指定
"""
companies = ['apple', 'facebook']
data = df.loc[companies]
data = data.sort_index()
data = data.T.reset_index()
data = data.head()
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
# st.altair_chart(chart, use_container_width=True)
st.altair_chart(chart)





_="""
21-グラフ化
  グラフ化したものを出力できない
  print(aapl.actions['Stock Splits'].plt)→×
  actionsは公式ドキュメント参考
"""
# aapl = yf.Ticker('AAPL')
# # print(aapl.info)
# aapl.actions.head()
# # plt.show(aapl.dividends.plot())
# aapl.actions['Stock Splits'].plt
