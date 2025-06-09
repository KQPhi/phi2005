import re
import streamlit as st

# Hàm làm sạch kí tự kp chữ cái và số
def clean_non_alphabetic(text):
    text = re.sub(r'[.,?!@#$%^&*()]','',text)
    return text

# Hàm làm sạch
def clean(text):
    text = text.lower() # viết thường
    text = clean_non_alphabetic(text) # bỏ kí tự đặc biệt
    text = re.sub(r' ',' ',text)
    return text
# Hàm tách từ trong câu
def tokenize(text):
    words = text.split(' ')
    return words

# Hàm đếm từ
def count_word(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

# Dữ liệu huấn luyện
train_spam = 'Nhanh tay nhận ngay khuyến mãi cực lớn! Hôm nay duy nhất, giảm giá tới 70% cho hàng ngàn sản phẩm hot nhất thị trường.Cơ hội chỉ đến một lần, đừng bỏ lỡ! Truy cập ngay http://khuyenmai-sieusoc.vn để đặt hàng với giá siêu sốc.Số lượng có hạn, ai nhanh tay thì được!' 
train_not_spam = 'Chào bạn, mình gửi thông báo về cuộc họp nhóm vào 9h sáng ngày mai tại phòng họp B2.Nội dung họp bao gồm báo cáo tiến độ, phân công việc tuần tới và thống nhất kế hoạch báo cáo.Bạn vui lòng chuẩn bị phần trình bày cá nhân và đến đúng giờ. Cảm ơn và hẹn gặp lại!'

# Huấn luyện dữ liệu spam
clean_spam = clean(train_spam)
spam_words = tokenize(clean_spam)
total_spam_words = len(spam_words)
spam_freq = count_word(spam_words)

# Huấn luyênj dữ liệu not spam
clean_not_spam = clean(train_not_spam)
not_spam_words = tokenize(clean_not_spam)
total_not_spam_words = len(not_spam_words)
not_spam_freq = count_word(not_spam_words)

# Danh scahs phân biệt các từ trong 2 bộ dữ liệu
vocab = []
vocab.extend(spam_words)
vocab.extend(not_spam_words)
vocab = set()
total_vocab = len(vocab)

# Hàm dự đoán
def predict(text):
    text = clean(text)
    words = tokenize(text)
    prob_spam = 0.5
    prob_not_spam = 0.5
    for word in words:
        # tính xác suất spam
        f_spam = spam_freq.get(word, 0) # nếu kh có thì gán gtri = 0
        p_spam = (f_spam + 1) / (total_spam_words + total_vocab)
        prob_spam = prob_spam * p_spam

        # tính xác suất not spam
        f_not_spam = not_spam_freq.get(word, 0)
        p_not_spam = (f_not_spam + 1) / (total_not_spam_words + total_vocab)
        prob_not_spam = prob_not_spam * p_not_spam
    if prob_spam >= prob_not_spam:
        print('spam')
    else:
        print('not spam')

# chạy vd
predict('Nhận ưu đãi cực sốc hôm nay')