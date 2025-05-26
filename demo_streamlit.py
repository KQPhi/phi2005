import streamlit as st
import datetime
st.title("hello, DP20201")

# Tính tuổi 

st.header("tinh tuoi")
nam_sinh = st.number_input("moi nhap nam sinh: ")

if nam_sinh:
    nam_hien_tai = 2025 # lay nam hien tai
    tuoi = nam_hien_tai - nam_sinh

    st.write(f"tuoi cua ban la: {tuoi} tuoi")


# tai len file va dem so luong tu

file_tal = st.file_uploader("tai len file van ban")

if file_tal is not None :
    noi_dung =  file_tal.read().decode("utf-8") # doc noi dung file
    do_dai = len(noi_dung)
    st.write(f"file co do dai {do_dai} tu ")