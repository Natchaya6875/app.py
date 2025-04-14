import streamlit as st

st.set_page_config(page_title="เลือกภาษา", layout="centered")

st.markdown("<h2 style='text-align: center;'>🌐 กรุณาเลือกภาษา</h2>", unsafe_allow_html=True)

# จัดเป็นตาราง 2x2
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.markdown("""
    <a href="?lang=th">
        <img src="https://flagcdn.com/w320/th.png" width="100"><br>
        <strong>ภาษาไทย</strong>
    </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="?lang=en">
        <img src="https://flagcdn.com/w320/us.png" width="100"><br>
        <strong>English</strong>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <a href="?lang=my">
        <img src="https://flagcdn.com/w320/mm.png" width="100"><br>
        <strong>ภาษาพม่า</strong>
    </a>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <a href="?lang=kh">
        <img src="https://flagcdn.com/w320/kh.png" width="100"><br>
        <strong>ภาษากัมพูชา</strong>
    </a>
    """, unsafe_allow_html=True)
