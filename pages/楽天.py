import yfinance as yf
import pandas as pd
import altair as alt
import streamlit as st
import datetime

dt = datetime.datetime.today()
t = dt.time().replace(second=0, microsecond=0)
# print(t)

tickers = {
    '楽天': '4755.T'
}
ticker = ['4755.T']

st.write("""
    # 詳細ページ
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader(list(tickers.keys())[0])

with col2:
    st.subheader('col2')



days = 20
tkr = yf.Ticker('4755.T')
hist = tkr.history(period=f'{days}d')
# print(hist)
# (period=f'{days}d')


# 取引時間外だとエラー？？

start = dt.today()
end = dt.today()+datetime.timedelta(days=1)
df = yf.download(ticker, start, end, interval="1m")["Close"] #intervalで1分を指定
# st.write(df.tail())

# if not df:
if df.empty:
    days = pd.to_datetime(hist.index)
    days = max(days)
    # st.write(days)
    # st.write(hist)
    # hist = hist.max(hist.index)
    hists = hist.loc[max(hist.index)]
    hists = hists.loc['Close']
    hists = hists.astype(str)
    st.write(hists)
    # st.write(hist[['Close']].hists)
    # st.write(hist[['Close']].days)
    
    days = days.strftime('%Y-%m-%d')
    st.write(days)
    # その日の終値　15時
else:
    # st.write(df.tail())
    st.write('aaaaaaaaaaaaaaaa')
    # リアルタイムの株価と時間を表示する


_="""
Open その日の始値
High その日の最高値
Low その日の最安値
Closeその日の終値
Volume その日の取引量
Dividends 配当金
Stock Splits 株式分割数
"""