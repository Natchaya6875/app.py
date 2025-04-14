import streamlit as st

# --- ข้อมูลพื้นฐาน ---
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
    # ภาษาพม่า เขมร อังกฤษ สามารถเพิ่มได้ในอนาคต
}

# --- เซสชันสำหรับจัดการหน้า ---
if 'page' not in st.session_state:
    st.session_state.page = 'language_select'
if 'language' not in st.session_state:
    st.session_state.language = 'th'

# --- ฟังก์ชันเปลี่ยนหน้า ---
def go_to_page(page_name):
    st.session_state.page = page_name
    st.experimental_rerun()

# --- หน้าเลือกภาษา ---
if st.session_state.page == 'language_select':
    st.title('👶 ระบบให้คำแนะนำสำหรับญาติทารกแรกเกิด')
    st.subheader('🌐 กรุณาเลือกภาษา / Please select a language:')
    cols = st.columns(4)
    for i, (code, info) in enumerate(languages.items()):
        with cols[i]:
            if st.button(f\"{info['flag']}\\n{info['name']}\"):
                st.session_state.language = code
                go_to_page('main_menu')

# --- หน้าหลักเมนู ---
elif st.session_state.page == 'main_menu':
    lang = st.session_state.language
    st.markdown(f\"## {languages[lang]['flag']} {languages[lang]['name']}\")
    st.subheader(\"📋 กรุณาเลือกหัวข้อ:\")
    if st.button(main_topics[lang][0]):
        go_to_page('video')
    if st.button(main_topics[lang][1]):
        go_to_page('disease_list')
    if st.button('🔄 เปลี่ยนภาษา / Change Language'):
        go_to_page('language_select')

# --- หน้าวิดีโอคำแนะนำ ---
elif st.session_state.page == 'video':
    lang = st.session_state.language
    st.subheader(main_topics[lang][0])
    st.markdown(f\"\"\"\n        <iframe width=\"100%\" height=\"315\" src=\"{videos[lang]}\"\n        frameborder=\"0\" allowfullscreen></iframe>\n    \"\"\", unsafe_allow_html=True)
    if st.button('🔙 กลับเมนู'):
        go_to_page('main_menu')

# --- หน้ารายชื่อโรคที่พบบ่อย ---
elif st.session_state.page == 'disease_list':
    lang = st.session_state.language
    st.subheader(main_topics[lang][1])
    st.markdown(\"🩺 โรคต่างๆในทารกแรกเกิดที่พบบ่อย:\")
    for disease in neonatal_diseases['th']:
        st.markdown(f\"- {disease}\")
    if st.button('🔙 กลับเมนู'):
        go_to_page('main_menu')

pip install streamlit
