import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門')

st.write('DisplayImage')

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)

'あなたが好きな数字は', option, 'です。'


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