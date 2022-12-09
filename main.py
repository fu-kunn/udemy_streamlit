import streamlit as st
import numpy as np
import pandas as pd

st.title('streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
  '1列目': [1, 10, 3, 4],
  '2列目': [10, 20, 30, 40]
})

# writeではなくdataframeにすると指定できる引数が増える
st.dataframe(df.style.highlight_max(axis=0), width=200, height=500)

# マークダウン記法
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""