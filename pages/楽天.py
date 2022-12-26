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
# 修正必要　前の日に株式市場が閉まっているとデータが取ってこれない
yesterday = days - 2

tkr = yf.Ticker('4755.T')
# 最新のニュース
news = tkr.news[0]
TITLE = news["title"]
URL = news["link"]

hist = tkr.history(period=f'{days}d')

# 取引時間外だとエラー？？
start = dt.today()
end = dt.today()+datetime.timedelta(days=-1)
# df = yf.download(ticker, start, end, interval='1m')['Close'] #intervalで1分を指定
df = yf.download(ticker, end, interval='1m')['Close']
# df = yf.download(ticker, end)['Close']
# st.write(df)
# st.write(df.loc[max(df.index)])

# 現在時刻 14:15→14
hour = df.index.max().hour

st.write("""
    # 詳細ページ
""")

_="""
銘柄名
株価
"""
col1, col2 = st.columns(2)
with col1:
    st.subheader(list(tickers.keys())[0])

with col2:
    _="""
    取得したデータが15時を含む以降であるとき
     15時を表示
     その日の終値を株価に表示
    """
    if hour >= 15:
        days = pd.to_datetime(hist.index)
        days = max(days)
        hists = hist.loc[max(hist.index)]
        delta = hist.iloc[yesterday]
        # st.write(delta)
        delta = delta.loc['Close']
        # st.write(delta)
        hists = hists.loc['Close']
        delta = hists - delta

        hists = hists.astype(str)

        days = days.strftime('%Y-%m-%d')
        st.subheader(days+' 15:00')

        st.metric(label='株価', value=f'{hists} 円', delta=f'{delta} 円')
        # st.subheader('株価： '+hists+'円')
        
    else:
        # 同じ内容を↑にも書いているためまとめる
        hists = hist.loc[max(hist.index)]
        delta = hist.iloc[yesterday]
        delta = delta.loc['Close']
        hists = hists.loc['Close']
        delta = hists - delta
        hists = df.loc[max(df.index)]
        # リアルタイムの株価と時間を表示する
        st.subheader(df.index.max())
        st.metric(label='株価', value=f'{hists} 円', delta=f'{delta} 円')

_="""
これから追加予定
Open その日の始値
High その日の最高値
Low その日の最安値
Closeその日の終値
Volume その日の取引量
Dividends 配当金
Stock Splits 株式分割数
"""




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
    columns={
        'value': '取引量',
        'Date': '日付'
    }
)
bar_chart = (
    alt.Chart(data)
    .mark_bar()
    .encode(
        x="日付:T",
        # y=alt.Y("Stock Prices:Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
        y=alt.Y("取引量:Q"),
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
    columns={
        'value': '株価',
        'Date': '日付'
    }
)
chart = (
    alt.Chart(data)
    .mark_line(opacity=0.8)
    .encode(
        x="日付:T",
        # y=alt.Y("Stock Prices:Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
        y=alt.Y("株価:Q", stack=None, scale=alt.Scale(domain=[400, 1200])),
        color='Name:N'
    )
)
st.altair_chart(chart, use_container_width=True)

# pd.concat([chart, bar_chart], axis=0)
# st.write(data['Date'])


# 最新ニュース
st.write("""
    #### 最新ニュース
""")
st.write('タイトル:')
st.write(TITLE)
st.write(URL)

_="""
Open その日の始値
High その日の最高値
Low その日の最安値
Closeその日の終値
Volume その日の取引量
Dividends 配当金
Stock Splits 株式分割数
"""