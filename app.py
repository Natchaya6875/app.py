import streamlit as st

# ตั้งค่าหน้าจอและพื้นหลัง
def set_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.pexels.com/photos/459905/pexels-photo-459905.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# คำแปลในแต่ละภาษา
translations = {
    "ไทย": {
        "welcome": "เลือกภาษา",
        "intro": "การแนะนำการปฏิบัติตัวแก่ญาติขณะรับใหม่",
        "diseases": "โรคต่างๆในทารกแรกเกิดที่พบบ่อย",
        "disease_list": [
            "ความดันเลือดที่ปอดสูง",
            "ทารกคลอดก่อนกำหนด",
            "ภาวะเลือดข้น",
            "ภาวะน้ำตาลในเลือดต่ำ",
            "ภาวะตัวเหลือง"
        ],
        "video_link": "https://www.youtube.com/watch?v=THzvG1KPgXk"
    },
    "မြန်မာစာ": {
        "welcome": "ဘာသာစကားရွေးပါ",
        "intro": "မိသားစုဝင်များအတွက်လမ်းညွှန်",
        "diseases": "လူနာကလေးများတွင်တွေ့ရသောရောဂါများ",
        "disease_list": [
            "အဆုတ်သွေးဖိအားမြင့်",
            "မလုံလောက်သောဖွားမှု",
            "အသည်းအသန်သွေးချင်း",
            "သွေးတွင်းသကြားနိမ့်ခြင်း",
            "အရောင်ပြောင်းခြင်း"
        ],
        "video_link": "https://www.youtube.com/watch?v=JZzjWnHJdcA"
    },
    "ភាសាខ្មែរ": {
        "welcome": "ជ្រើសរើសភាសា",
        "intro": "ការណែនាំដល់គ្រួសារពេលទទួលទារក",
        "diseases": "ជំងឺដែលជួបប្រទះញឹកញាប់",
        "disease_list": [
            "សំពាធឈាមខ្ពស់នៅសួត",
            "ទារកកើតមិនទាន់ពេល",
            "សភាពឈាមខាប់",
            "ស្ករក្នុងឈាមទាប",
            "ជាតិលឿងក្នុងខ្លួន"
        ],
        "video_link": "https://www.youtube.com/watch?v=jKhkhna9g5Q"
    },
    "English": {
        "welcome": "Select a language",
        "intro": "Guidelines for Families at Admission",
        "diseases": "Common Neonatal Diseases",
        "disease_list": [
            "Pulmonary Hypertension",
            "Premature Birth",
            "Polycythemia",
            "Hypoglycemia",
            "Jaundice"
        ],
        "video_link": "https://www.youtube.com/watch?v=BLZxH-3f6fI"
    }
}

# ฟังก์ชันแต่ละหน้า
def main():
    set_background()

    if 'language' not in st.session_state:
        st.session_state.language = None
    if 'page' not in st.session_state:
        st.session_state.page = 1

    # หน้าที่ 1: เลือกภาษา
    if st.session_state.page == 1:
        st.header("👶 NICU Information")
        st.subheader("🌐 " + "Select Language / เลือกภาษา")

        cols = st.columns(4)
        languages = ["ไทย", "မြန်မာစာ", "ភាសាខ្មែរ", "English"]
        flags = ["🇹🇭", "🇲🇲", "🇰🇭", "🇺🇸"]
        for i, lang in enumerate(languages):
            if cols[i].button(f"{flags[i]} {lang}"):
                st.session_state.language = lang
                st.session_state.page = 2

    # หน้าที่ 2: หัวข้อหลัก
    elif st.session_state.page == 2:
        lang = st.session_state.language
        st.subheader(translations[lang]["welcome"])
        if st.button("📹 " + translations[lang]["intro"]):
            st.session_state.page = "video"
        if st.button("📚 " + translations[lang]["diseases"]):
            st.session_state.page = 4

    # หน้าที่ 3: วิดีโอแนะนำ
    elif st.session_state.page == "video":
        lang = st.session_state.language
        st.video(translations[lang]["video_link"])
        if st.button("🔙 กลับ / Back"):
            st.session_state.page = 2

    # หน้าที่ 4: รายชื่อโรค
    elif st.session_state.page == 4:
        lang = st.session_state.language
        st.subheader("📖 " + translations[lang]["diseases"])
        for disease in translations[lang]["disease_list"]:
            st.markdown(f"- {disease}")
        if st.button("🔙 กลับ / Back"):
            st.session_state.page = 2

if __name__ == "__main__":
    main()
