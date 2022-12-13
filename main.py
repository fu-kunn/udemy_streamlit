import streamlit as st
import time

st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_itreation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_itreation.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'

# st.beta_columns(2)だとエラーになる
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右カラムです！')

for i in range(1, 4):
  expander = st.expander('問い合わせ' + str(i))
  expander.write('問い合わせ' + str(i) + 'の回答')

# condition = st.slider(
#   'あなたの調子は？', 0, 100, 50
# )
# 'あなたのコンディションは　', condition, 'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('mulsol.JPG')
#     st.image(img, caption='MulSol', use_column_width=True)

_="""
streamlitでの複数行コメントの方法
"""

_="""
'lat', 'lon'→緯度・経度
[35.69, 139,79]新宿付近の緯度と経度を足してその付近を表している
"""
# df = pd.DataFrame(
#   np.random.rand(100, 2)/[50, 50] + [35.69, 139.79],
#   columns=['lat', 'lon']
# )
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)
# st.map(df)

_="""
writeではなくdataframeにすると指定できる引数が増える
st.dataframe(df.style.highlight_max(axis=0), width=200, height=500)
"""

# マークダウン記法
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """