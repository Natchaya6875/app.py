import streamlit as st

# ข้อมูล
languages = {
    'th': {'name': 'ภาษาไทย', 'flag': '🇹🇭'},
    'my': {'name': 'မြန်မာစာ', 'flag': '🇲🇲'},
    'km': {'name': 'ភាសាខ្មែរ', 'flag': '🇰🇭'},
    'en': {'name': 'English', 'flag': '🇬🇧'}
}

main_topics = {
    'th': ['การแนะนำการปฏิบัติตัวแก่ญาติขณะรับใหม่', 'โรคต่างๆในทารกแรกเกิดที่พบบ่อย'],
    'my': ['သွားရောက်လည်ပတ်သူများအတွက်ညွှန်ကြားချက်', 'လူငယ်ကလေးများတွင်တွေ့ရသောရောဂါများ'],
    'km': ['ការណែនាំចំពោះសាច់ញាតិក្នុងពេលទទួលទាន', 'ជំងឺដែលជួបប្រទៈញឹកញាប់នៅក្នុងទារក'],
    'en': ['Guidance for Relatives During Admission', 'Common Neonatal Diseases']
}

videos = {
    'th': 'https://www.youtube.com/embed/thai_video_id',
    'my': 'https://www.youtube.com/embed/myanmar_video_id',
    'km': 'https://www.youtube.com/embed/khmer_video_id',
    'en': 'https://www.youtube.com/embed/english_video_id'
}

neonatal_diseases = {
    'th': [
        'ความดันเลือดที่ปอดสูง',
        'ทารกคลอดก่อนกำหนด',
        'ภาวะเลือดข้น',
        'ภาวะน้ำตาลในเลือดต่ำ',
        'ภาวะตัวเหลือง'
    ]
    # เพิ่มภาษาอื่นได้ในอนาคต
}

# เริ่ม Streamlit App
if 'language' not in st.session_state:
    st.session_state.language = None

st.title(\"👶 แอปให้ความรู้สำหรับญาติของทารกแรกเกิด\")

# หน้า 1: เลือกภาษา
if st.session_state.language is None:
    st.header(\"🌐 กรุณาเลือกภาษา / Please select a language:\")
    for code, info in languages.items():
        if st.button(f\"{info['flag']} {info['name']}\"):
            st.session_state.language = code
            st.rerun()

# หน้า 2: เมนูหัวข้อ
else:
    lang = st.session_state.language
    st.header(f\"{languages[lang]['flag']} {languages[lang]['name']}\")
    
    st.subheader(\"📋 กรุณาเลือกหัวข้อ:\")
    topic = st.radio(\"\", main_topics[lang])

    # หน้า 3: วิดีโอคำแนะนำ
    if topic == main_topics[lang][0]:
        st.markdown(\"\"\"<iframe width='100%' height='315' src='{}' frameborder='0' allowfullscreen></iframe>\"\"\".format(videos[lang]), unsafe_allow_html=True)
        if st.button(\"🔙 กลับเมนู / Back to Menu\"):
            st.rerun()

    # หน้า 4: รายชื่อโรค
    elif topic == main_topics[lang][1]:
        st.subheader(\"🩺 รายชื่อโรคที่พบบ่อย:\")
        for disease in neonatal_diseases['th']:  # ปรับตามภาษาถ้าเพิ่มแล้ว
            st.markdown(f\"- {disease}\")
        if st.button(\"🔙 กลับเมนู / Back to Menu\"):
            st.rerun()