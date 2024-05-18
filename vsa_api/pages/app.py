import streamlit as st
from vsa_api.services import sent_analysis_service

st.set_page_config(
        page_title="Vietnamese Sentiment Analysis"
)

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
            with st.spinner('Wait for it...'):
                evaluate = sent_analysis_service(sentence)
                if evaluate > 0.5:
                    st.success("Cảm ơn những đánh giá tích cực bạn!")
                else:
                    st.success("Xin lỗi bạn vì chất lượng của bộ phim! Chúng tôi sẽ **khắc phục** trong tương lai")
        else:
            st.warning("Vui lòng nhập bình luận!")
