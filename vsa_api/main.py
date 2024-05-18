from st_pages import Page, show_pages
import streamlit as st


# Specify what pages should be shown in the sidebar, and what their titles 
# and icons should be
show_pages(
    [
        Page("../Sentiment_Analysis_Vietnamese/vsa_ap/main.py", "Introduction", ":brain:"),
        Page("../Sentiment_Analysis_Vietnamese/vsa_ap/pages/app.py", "Application", ":video_game:"),
        Page("../Sentiment_Analysis_Vietnamese/vsa_ap/pages/members.py", "Member", ":adult:")
    ]
)

st.write("""
# :brain: Giới thiệu chung
""")
