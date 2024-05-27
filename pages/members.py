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
# :adult: Thành viên

### Nhóm gồm hai thành viên:
""")

col1, col2 = st.columns([1, 1])

with col1:
    st.image("../Sentiment_Analysis_Vietnamese/images/Duc1.jpg", caption="Huỳnh Trọng Đức - 21IT129")
    st.write("""
    - Vai trò: Member
    - Họ tên: Huỳnh Trọng Đức
    - Mã sinh viên: 21IT129
    - Lớp sinh hoạt: 21SE3
    - Khoa: Khoa Học Máy Tính
    - Ngành: Công Nghệ Thông Tin
    """)

with col2:
    st.image("../Sentiment_Analysis_Vietnamese/images/Nam.jpg", caption="Võ Văn Nam - 21IT683")
    st.write("""
    - Vai trò: Leader
    - Họ tên: Võ Văn Nam
    - Mã sinh viên: 21IT683
    - Lớp sinh hoạt: 21SE3
    - Khoa: Khoa Học Máy Tính
    - Ngành: Công Nghệ Thông Tin
    """)

st.markdown("""
### Github: [Github Of Application](https://github.com/NamVo181203/Sentiment_Analysis_Vietnamese)

### Driver: [Driver Of Model](https://drive.google.com/drive/folders/1-KxZ3F_8OGifimZXUuQkeL7ZDSyUnvN5?usp=sharing)
""")
