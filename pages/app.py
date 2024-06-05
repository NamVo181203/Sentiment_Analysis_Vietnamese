import streamlit as st
import requests
from supabase import create_client, Client

# init DB
url: str = "https://gbvvdcnaevbzetbrvmdc.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdidnZkY25hZXZiemV0YnJ2bWRjIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxNjc5MjAzMCwiZXhwIjoyMDMyMzY4MDMwfQ.j9CIUk_VOWL0lLf8WJuyGY4C5l0qjhmmru53nSONXG8"
DB: Client = create_client(supabase_url=url, supabase_key=key)


# Goi API
def get_sentiment(text):
    url = 'http://127.0.0.1:8000/predict_sentiment'  # Địa chỉ API của bạn
    response = requests.post(url, json={'text': text})
    if response.status_code == 200:
        return response.json()['sentiment']
    else:
        return 'Error'


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
                sentiment = get_sentiment(sentence)
                print(f"Sentiment: {sentiment}")
                if sentiment > 0.5:
                    st.success("Cảm ơn những đánh giá tích cực bạn!")
                    insert_data = {"film_url": dict_film[option], "predict": "positive"}
                    # Insert vào bảng
                    response = DB.table("comment").insert(insert_data).execute()
                    print(f"DB: {response}")

                else:
                    st.success("Xin lỗi bạn vì chất lượng của bộ phim! Chúng tôi sẽ **khắc phục** trong tương lai")
                    insert_data = {"film_url": dict_film[option], "predict": "negative"}
                    # Insert vào bảng
                    response = DB.table("comment").insert(insert_data).execute()
                    print(f"DB: {response}")

        else:
            st.warning("Vui lòng nhập bình luận!")
