import streamlit as st
import yfinance as yf
import pandas as pd
import altair as alt

st.title('株価可視化アプリ')

st.sidebar.write("""
    # 株価
    こちらは株価可視化ツールです。以下のオプションから表示日数を指定して下さい。
""")

st.sidebar.write("""
    ## 表示日数選択
""")

days = st.sidebar.slider('日数', 1, 50, 20)

st.write(f"""
    ### 過去 **{days}日間** の株価
""")


tickers = {
    '無印良品': '7453.T',
    '楽天': '4755.T',
    'サンドラック': '9989.T',
    'トヨタ自動車': '7203.T',
}

@st.cache
def get_data(days, tickers):
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
    return df

try:
    st.write("""
        ### 株価の範囲指定
    """)

    ymin, ymax = st.sidebar.slider(
      '範囲を指定して下さい', 0.0, 4000.0, (0.0, 4000.0)
    )

    df = get_data(days, tickers)
    companies = st.multiselect(
        '会社名を選択して下さい。',
        list(df.index),
        ['楽天', '無印良品']
    )

    if not companies:
        st.error('少なくとも一社は選択して下さい。')
    else:
        data = df.loc[companies]
        st.write('### 株価', data.sort_index())
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=['Date']).rename(
            columns={'value': 'Stock Prices'}
        )
        chart = (
            alt.Chart(data)
            .mark_line(opacity=0.8)
            .encode(
                x="Date:T",
                y=alt.Y("Stock Prices:Q", stack=None, scale=alt.Scale(domain=[ymin, ymax])),
                color='Name:N'
            )
        )
        st.altair_chart(chart, use_container_width=True)
except:
    st.error(
        'エラーです！！'
    )