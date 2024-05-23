from st_pages import Page, show_pages
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

# Specify what pages should be shown in the sidebar, and what their titles
# and icons should be
show_pages(
    [
        Page("../Sentiment_Analysis_Vietnamese/vsa_api/main.py", "Introduction", ":brain:"),
        Page("../Sentiment_Analysis_Vietnamese/vsa_api/pages/members.py", "Member", ":adult:"),
        Page("../Sentiment_Analysis_Vietnamese/vsa_api/pages/app.py", "Application", ":video_game:"),
        Page("../Sentiment_Analysis_Vietnamese/vsa_api/pages/evaluate_model.py", "Evaluate Model", ":scales:"),
    ]
)

st.write("""
# :brain: Giới thiệu chung
Trong những năm gần đây, phân tích và nhận diện cảm xúc ngày càng trở nên phổ biến để xử lý dữ liệu truyền thông xã hội trên các cộng đồng trực tuyến, blog, wiki, nền tảng tiểu blog và các phương tiện cộng tác trực tuyến khác. Phân tích nhận diện cảm xúc là một nhánh của nghiên cứu điện toán sinh thái nhằm phân loại văn bản (nhưng đôi khi cả âm thanh và video ) thành tích cực hoặc tiêu cực.

Đây là một lĩnh vực liên quan đến truy xuất thông tin và tổng hợp thông tin vì nó yêu cầu dữ liệu phải được thu thập, tích hợp và phân loại. Hầu hết các tài liệu về ngôn ngữ tiếng Anh nhưng gần đây ngày càng có nhiều ấn phẩm đề cập đến vấn đề đa ngôn ngữ. Hệ thống phân tích nhận diện cảm xúc có thể được phân loại rộng rãi thành dựa trên tri thức và dựa trên thống kê. Trong khi hầu hết các công việc áp dụng nó như là một bài toán phân loại đơn giản, phân tích cảm xúc là một bài toán nghiên cứu đòi hỏi phải giải quyết nhiều nhiệm vụ NLP (Natural Language Processing), bao gồm nhận dạng thực thể được đặt tên, trích xuất khái niệm, phát hiện châm biếm, trích xuất khía cạnh và phát hiện tính chủ quan. Phát hiện tính chủ quan là một nhiệm vụ cần thiết của phân tích cảm xúc vì hầu hết các công cụ phát hiện cảm tính đều được tối ưu hóa để phân biệt giữa văn bản tích cực và tiêu cực

Hiện tại thì cộng đồng khoa học mới chỉ giải quyết tốt bài toán phân tích và nhận diện cảm xúc trong văn bản tiếng Việt ở cấp độ đơn giản, tức là phân tích cảm xúc với hai lớp cảm xúc tiêu cực và tích cực với độ chính xác hơn 85%. Bài toán phân tích cảm xúc có một số phương pháp giải quyết như sau:

- Phương pháp thủ công (dò từ khóa): việc dự đoán cảm xúc dựa vào việc tìm kiếm các từ cảm xúc riêng lẻ, xác định điểm số cho các từ tích cực, xác định điểm số cho các từ tiêu cực và sau đó là tổng hợp các điểm số này lại theo một độ đo xác định để quyết định xem văn bản mang màu sắc cảm xúc gì. Điểm hạn chế của phương pháp này là quan tâm đến thứ tự các từ và sẽ bỏ qua các từ quan trọng. Độ chính xác của mô hình phụ thuộc vào độ tốt của bộ từ điển các từ cảm xúc.Ưu điểm của phương pháp này là dễ thực hiện, tính toán nhanh, chỉ tốn công sức cho việc xây dựng bộ từ điển dữ liệu của các từ cảm xúc thôi.
- Phương pháp Deep Learning Neural Network: phương pháp phân tích nhận diện cảm xúc đã được giải quyết bằng mô hình học Recurrent Neural Network với một phương pháp được dùng phổ biến hiện nay là Long Short Term Memory Neural Network (LSTMs), kết hợp với phương pháp mô hình vector hóa từ Word2Vector với kiến trúc được sử dụng là Continuous Bag- of-Words (CBOW).
- Phương pháp kết hợp rule-based và corpus-based: Phương pháp này kết hợp sử dụng mô hình Deep Learning Recursive Neural Network với hệ tri thức chuyên gia được sử dụng trong xử lý ngôn ngữ tự nhiên được gọi là Sentiment Treebank. Sentiment Tree là một mô hình cây phân tích cú pháp của một câu văn, trong đó ở mỗi nút trong cây được kèm theo bộ trọng số cảm xúc lần lượt là: rất tiêu cực, tiêu cực, trung tính, tích cực và rất tích cực.
""")
