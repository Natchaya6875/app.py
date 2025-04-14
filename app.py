import streamlit as st

st.set_page_config(page_title="แอปแนะนำผู้ปกครอง", page_icon="👶")

st.title("👶 แอปให้คำแนะนำผู้ปกครองทารกแรกเกิด")
st.write("ยินดีต้อนรับสู่ระบบให้คำแนะนำเบื้องต้นสำหรับพ่อแม่ของทารกที่นอนโรงพยาบาล")

language = st.selectbox("เลือกภาษา", ["ไทย", "อังกฤษ", "พม่า", "กัมพูชา"])

if language == "ไทย":
    st.subheader("📍 สถานที่")
    st.write("หอผู้ป่วยทารกแรกเกิดป่วย อาคารเฉลิมพระเกียรติ ตึกกุมารชั้น 3" \
    "ซึ่งเข้าเยี่ยมได้เฉพาะบิดามารดาเท่านั้น ")

    st.subheader("⏰ เวลาเข้าเยี่ยม")
    st.write("ทุกวัน เช้า เวลา 07.00 - 08.00 น. บ่าย เวลา 12.00 - 15.00 น. และเย็น เวลา 17.00 - 20.00 น.")

    st.subheader("🧳 สิ่งที่ต้องเตรียมมาให้ทารก")
    st.write("บัตรประชาชนของพ่อแม่, ทิชชู่, แพมเพิส, น้ำนมที่ปั๊มแล้ว")

    st.subheader("🍼 การบีบเก็บและนำน้ำนมมาส่ง")
    st.write("เก็บน้ำนมในถุงสะอาด เขียนชื่อ-วันที่ นำส่งห้องเก็บน้ำนมทุกวัน")

    st.subheader("🧾 การแจ้งเกิดและขอใช้สิทธิ์ค่ารักษาพยาบาล")
    st.write("1.แจ้งที่หน้าห้องคลอด ตึกชลารักษ์ ชั้น1")
    st.write("2.ติดต่อตึกทารกแรกเกิดป่วย นำเอกสารทั้งหมดไปที่ชั้น 2 ตึกกุมาร ห้องเบอร์ 1 " 
    "เพื่อทำการเปลี่ยนชื่อ นามสกุล ที่แจ้งเกิดใส่ในเอกสารของโรงพยาบาลแล้วนำเอกสารไปที่ห้องเบอร์ 2 " \
    "หรือ 3 เพื่อตรวจสอบสิทธิ์ รอรับเอกสารคืน")
    st.write("3.นำเอกสารกลับมาให้เจ้าหน้าที่ ที่หอผู้ป่วยทารกแรกเกิดป่วย")
    st.markdown("[🔗 คลิกไปที่เอกสารสิทธิการรักษา](https://drive.google.com/file/d/1Z57VmKNYXjq4gUFkOn7I_7pJLFtHs3UJ/view?usp=sharing)")

    st.subheader("🏥 การตรวจสอบสิทธิการรักษา")
    st.write("ตรวจสอบที่เว็บไซต์ สปสช. หรือโทร 1330")
    st.markdown("[ตรวจสอบสิทธิ์รักษา คลิกที่นี่](https://www.nhso.go.th/)")

    st.subheader("📞 การโทรสอบถามอาการ")
    st.write("โทร 03-893-2225 ต่อ 7")
else:
    st.info("ภาษานี้ยังอยู่ในระหว่างการพัฒนา โปรดลองเลือกภาษาไทยก่อนนะคะ 🧸")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.pexels.com/photos/459905/pexels-photo-459905.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
        background-size: cover;
        background-attachment: fixed;
        color: black;
    }

    /* เปลี่ยนสีตัวอักษรหลัก */
    .stMarkdown, .stText, .stTitle, .stHeader, .stSubheader, .stDataFrame, .stTextInput {
        color: black !important;
    }

    /* เปลี่ยนสีหัวข้อและกล่องข้อความอื่น ๆ */
    h1, h2, h3, h4, h5, h6, p {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)