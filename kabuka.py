import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import yfinance as yf
import altair as alt

# AAPL=ティッカーシンボル
# aapl = yf.Ticker('AAPL')
# muzi = yf.Ticker('7453.T')

# hist = aapl.history(period=f'{days}d')
# hist_muzi = muzi.history(period=f'{days}d')
# print(pd.concat([hist, hist_muzi], axis=1).head())

st.title('株価可視化アプリ')

st.sidebar.write("""
# 株価
こちらは株価可視化ツールです。以下のオプションから表示日数をして下さい。
""")

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

ymin, ymax = 120, 160
chart = (
  alt.Chart(data)
  .mark_line(opacity=0.8, clip=True)
  .encode(
    x="Date:T",
    y=alt.Y("Stock Prices:Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
    color='Name:N'
  )
)
st.altair_chart(chart, use_container_width=True)
# st.altair_chart(chart)





_="""
21-グラフ化
  グラフ化したものを出力できない
  print(aapl.actions['Stock Splits'].plot())→×
  actionsは公式ドキュメント参考
"""
# aapl = yf.Ticker('AAPL')
# # aapl.info
# # aapl.actions.head()
# # aapl.dividends.plot()
# # aapl.actions['Stock Splits'].plot()
# st.altair_chart(aapl.actions['Stock Splits'].plot())
