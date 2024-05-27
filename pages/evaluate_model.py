import pandas as pd
import streamlit as st

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/1RVtj3Ym/image.jpg");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] {{
background-color: #35373B;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.write("""
# :scales: Đánh giá mô hình

## Bảng đánh giá trong quá trình train
""")

header = ['Time(s)', 'Train Loss', 'Train Acc', 'Validation Loss', 'Validation Acc']
data = [['112s', '0.653', '65.11%', '0.711', '63.02%'],
        ['113s', '0.456', '75.98%', '0.582', '74.22%'],
        ['113s', '0.221', '85.56%', '0.378', '83.12%'],
        ['113s', '0.191', '92.49%', '0.259', '90.01%'],
        ['112s', '0.131', '95.41%', '0.247', '90.33%']]

tb_eval = pd.DataFrame(data, columns=header)

st.table(tb_eval)

st.write("## Bảng đánh giá trong quá trình test")

header_test = ['Time(s)', 'Test Loss', 'Test Acc']
data_test = [['4s', '0.290', '89.48%']]

tb_test = pd.DataFrame(data_test, columns=header_test)

st.table(tb_test)
