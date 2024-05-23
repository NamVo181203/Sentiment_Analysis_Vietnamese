import pandas as pd
import streamlit as st
from vsa_api.services import sent_analysis_service

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

st.markdown(
    """
<style>
button {
    padding-top: 7px !important;
    padding-bottom: 7px !important;
}
</style>
""",
    unsafe_allow_html=True,
)

st.write("""
# :video_game: Vietnamese Sentiment Analysis
""")

dict_film = {
    "Tội ác hoàn hảo": "https://www.youtube.com/watch?v=gtWdrlcJHBo&list=PLlFsTHwHfQWOBZtQbdUPZfB6fQ7Gc92Bh&index=1",
    "Luyện ngải: Cô hồn giả quỷ": "https://www.youtube.com/watch?v=Oz-MCOD8UNA&list=PLlFsTHwHfQWOBZtQbdUPZfB6fQ7Gc92Bh&index=2&pp=iAQB",
    "Haikyu!!: Trận Chiến Bãi Phế Liệu": "https://www.youtube.com/watch?v=OFB4mrupFX0&list=PLlFsTHwHfQWOBZtQbdUPZfB6fQ7Gc92Bh&index=5&pp=iAQB",
    "TRANSFORMERS MỘT": "https://www.youtube.com/watch?v=VPciAy7Tm94&list=PLlFsTHwHfQWOBZtQbdUPZfB6fQ7Gc92Bh&index=14&pp=iAQB"
}

option = st.selectbox("Trailer phim:",
                      ("Haikyu!!: Trận Chiến Bãi Phế Liệu", "Luyện ngải: Cô hồn giả quỷ", "Tội ác hoàn hảo",
                       "TRANSFORMERS MỘT"),
                      index=None,
                      placeholder="Chọn trailer phim bạn muốn...",
                      )
if option:
    st.video(dict_film[option])

sentence = st.text_input("Bình luận về trailer:", placeholder="Phim khiến cho tôi cảm thấy...")

if st.button("Đánh giá", use_container_width=True):
    if not option:
        st.warning("Vui lòng xem trailer trước khi đánh giá!")
    else:
        if sentence:
            with st.spinner('Đợi trong giây lát để nhận được phản hồi...'):
                evaluate = sent_analysis_service(sentence)
                if evaluate > 0.5:
                    st.success("Cảm ơn những đánh giá tích cực bạn!")
                    header = ['review', 'sentiment']
                    data = [[str(sentence), "positive"]]
                    data = pd.DataFrame(data, columns=header)
                    data.to_csv("./dataset/data/comment_evaluate.csv",
                                index=False)
                else:
                    st.success("Xin lỗi bạn vì chất lượng của bộ phim! Chúng tôi sẽ **khắc phục** trong tương lai")
                    header = ['review', 'sentiment']
                    data = [[str(sentence), "negative"]]
                    data = pd.DataFrame(data, columns=header)
                    data.to_csv("./dataset/data/comment_evaluate.csv",
                                index=False)
        else:
            st.warning("Vui lòng nhập bình luận!")
