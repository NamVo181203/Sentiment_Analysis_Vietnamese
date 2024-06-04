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

### Nhóm gồm các thành viên:
""")

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

with col1:
    st.image("images/Nam.jpg", caption="Võ Văn Nam")
    st.write("""
    - Vai trò: Leader
    - Họ tên: Võ Văn Nam
    - Mã sinh viên: 21IT683
    - Lớp sinh hoạt: 21SE3
    - Khoa: Khoa Học Máy Tính
    - Ngành: Công Nghệ Thông Tin
    """)

with col2:
    st.image("images/Duc.jpg", caption="Huỳnh Trọng Đức")
    st.write("""
    - Vai trò: Member
    - Họ tên: Huỳnh Trọng Đức
    - Mã sinh viên: 21IT129
    - Lớp sinh hoạt: 21SE3
    - Khoa: Khoa Học Máy Tính
    - Ngành: Công Nghệ Thông Tin
    """)

with col3:
    st.image("images/Huy.jpg", caption="Nguyễn Viết Huy")
    st.write("""
    - Vai trò: Member
    - Họ tên: Nguyễn Viết Huy
    - Mã sinh viên: 21IT684
    - Lớp sinh hoạt: 21SE3
    - Khoa: Khoa Học Máy Tính
    - Ngành: Công Nghệ Thông Tin
    """)

with col4:
    st.image("images/Linh.jpg", caption="Ngô Nguyễn Viết Lĩnh")
    st.write("""
    - Vai trò: Member
    - Họ tên: Ngô Nguyễn Viết Lĩnh
    - Mã sinh viên: 21IT150
    - Lớp sinh hoạt: 21SE3
    - Khoa: Khoa Học Máy Tính
    - Ngành: Công Nghệ Thông Tin
    """)

st.markdown("""
### Github: [Github Of Application](https://github.com/NamVo181203/Sentiment_Analysis_Vietnamese)

### Driver: [Driver Of Model](https://drive.google.com/drive/folders/1-KxZ3F_8OGifimZXUuQkeL7ZDSyUnvN5?usp=sharing)

### Website: [Website Of Team](https://sentiment-analysis-vietnamese.streamlit.app)
""")
