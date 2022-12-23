import yfinance as yf
import pandas as pd
import altair as alt
import streamlit as st
import datetime

# t=日付のみ
dt = datetime.datetime.today()
t = dt.time().replace(second=0, microsecond=0)

tickers = {
    '楽天グループ': '4755.T'
}
ticker = ['4755.T']

days = 90
tkr = yf.Ticker('4755.T')
hist = tkr.history(period=f'{days}d')


# 取引時間外だとエラー？？
start = dt.today()
end = dt.today()+datetime.timedelta(days=1)
df = yf.download(ticker, start, end, interval="1m")["Close"] #intervalで1分を指定
# st.write(df.tail())

st.write("""
    # 詳細ページ
""")

col1, col2 = st.columns(2)
with col1:
    st.subheader(list(tickers.keys())[0])

with col2:
    if df.empty:
        days = pd.to_datetime(hist.index)
        days = max(days)
        hists = hist.loc[max(hist.index)]
        hists = hists.loc['Close']
        hists = hists.astype(str)
        st.metric(label='株価', value=f'{hists} 円', delta=f'{hists} 円')
        # st.subheader('株価： '+hists+'円')
        
        days = days.strftime('%Y-%m-%d')
        st.write(days+' 15:00')
        # その日の終値　15時
    else:
        # st.write(df.tail())
        st.write('aaaaaaaaaaaaaaaa')
        # リアルタイムの株価と時間を表示する



# 折れ線グラフ
st.write("""
    #### 株価チャート
""")
volume = hist[['Volume']]
# st.write(volume)
volume.columns = ['楽天グループ']
volume = volume.T
volume.index.name = 'Name'
df = pd.concat([df, volume])
data = volume
data = data.T.reset_index()
data = pd.melt(data, id_vars=['Date']).rename(
    columns={'value': 'Stock Prices'}
)
bar_chart = (
    alt.Chart(data)
    .mark_bar()
    .encode(
        x="Date:T",
        # y=alt.Y("Stock Prices:Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
        y=alt.Y("Stock Prices:Q"),
        color='Name:N'
    )
)
st.altair_chart(bar_chart, use_container_width=True)


hist = hist[['Close']]
hist.columns = ['楽天グループ']
hist = hist.T
hist.index.name = 'Name'
df = pd.concat([df, hist])
data = hist
data = data.T.reset_index()
data = pd.melt(data, id_vars=['Date']).rename(
    columns={'value': 'Stock Prices'}
)
chart = (
    alt.Chart(data)
    .mark_line(opacity=0.8)
    .encode(
        x="Date:T",
        # y=alt.Y("Stock Prices:Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
        y=alt.Y("Stock Prices:Q", stack=None, scale=alt.Scale(domain=[200, 1400])),
        color='Name:N'
    )
)
st.altair_chart(chart, use_container_width=True)

# pd.concat([chart, bar_chart], axis=0)
# st.write(data['Date'])

_="""
Open その日の始値
High その日の最高値
Low その日の最安値
Closeその日の終値
Volume その日の取引量
Dividends 配当金
Stock Splits 株式分割数
"""