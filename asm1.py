import streamlit as st

# Dữ liệu huấn luyện thủ công
data = [
    ("Messi ghi bàn trong trận bóng", "Thể thao"),
    ("Chính phủ công bố gói hỗ trợ kinh tế", "Thời sự"),
    ("Apple ra mắt iPhone mới", "Công nghệ"),
    ("Real Madrid vô địch La Liga", "Thể thao"),
    ("AI đang thay đổi thế giới", "Công nghệ"),
    ("Giá xăng giảm mạnh trong tháng qua", "Thời sự"),
]

# Danh sách stopword đơn giản
stop_words = ["trong", "ra", "mới", "và", "đang", "với", "của", "la", "tháng", "qua", "công", "bố", "gói"]

# Hàm chuẩn hóa và loại bỏ stopword
def clean_text(text):
    text = text.lower()
    for ch in ".,!?;:-":
        text = text.replace(ch, "")
    tokens = text.split()
    tokens = [t for t in tokens if t not in stop_words]
    return tokens

# Hàm phân loại dựa trên từ khóa
def classify(text):
    words = clean_text(text)
    scores = {"Thể thao": 0, "Thời sự": 0, "Công nghệ": 0}
    keywords = {
        "Thể thao": ["bóng", "messi", "trận", "real", "vô", "địch", "la", "liga","ghi","bàn","kiến","tạo","chuyền","boxing","MMA","võ","sĩ"],
        "Thời sự": ["chính", "phủ", "hỗ", "trợ", "kinh", "tế", "xăng", "giá", "tăng"],
        "Công nghệ": ["iphone", "apple", "ai", "công", "nghệ", "thay", "đổi"]
    }

    for category, kws in keywords.items():
        for word in words:
            if word in kws:
                scores[category] += 1

    predicted = max(scores, key=scores.get)
    return predicted if scores[predicted] > 0 else "Không xác định"

# Giao diện Streamlit
st.title("Phân loại văn bản (phiên bản nhẹ)")
st.write("Nhập nội dung văn bản để xác định thể loại:")

user_input = st.text_area("Nhập văn bản:")

if st.button("Phân loại"):
    if user_input.strip() == "":
        st.warning("Vui lòng nhập văn bản.")
    else:
        prediction = classify(user_input)
        st.success(f"Thể loại dự đoán: **{prediction}**")