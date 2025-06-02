import streamlit as st

st.header("bai 1 lab4.1")
file_tal = st.file_uploader("tai len file",type="txt")

if file_tal is not None:
    noi_dung = file_tal.read().decode("utf-8")
    ls_tu = noi_dung.replace(",","").replace(".","")
    tach_tu = ls_tu.split()
    ds_tu = {}

    for tu in tach_tu:
        if tu not in ds_tu:
            ds_tu[tu] = 1
        else:
            ds_tu[tu] += 1
    st.write(ds_tu)

    save_name = "tan_suat_tu.txt"
    with open(save_name, "w", encoding="utf-8") as f:
        for tu, soluong in ds_tu.items():
            f.write(f"{tu} : {soluong}\n")


    with open(save_name, "rb") as f:
        st.download_button("tai len file", f, file_name=save_name, mime="text/plain")


st.header("bai 2 lab4.1")

file_tanso = st.file_uploader("tai len file tan suat tu", type="txt")


if file_tanso is not None:
        noi_dung = file_tanso.read().decode("utf-8")
        tu_dien = {}
        for dong in noi_dung.strip().split("\n"):
            if ":" in dong:
                tu, sl = dong.split(":", 1)
                tu_dien[tu.strip()] = int(sl.strip())
        
        st.write(tu_dien)