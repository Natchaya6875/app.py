from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# ภาษาและธงชาติ
languages = {
    'th': {'name': 'ภาษาไทย', 'flag': '🇹🇭'},
    'my': {'name': 'မြန်မာစာ', 'flag': '🇲🇲'},
    'km': {'name': 'ភាសាខ្មែរ', 'flag': '🇰🇭'},
    'en': {'name': 'English', 'flag': '🇬🇧'}
}

# ข้อความหัวข้อหลัก
main_topics = {
    'th': ['การแนะนำการปฏิบัติตัวแก่ญาติขณะรับใหม่', 'โรคต่างๆในทารกแรกเกิดที่พบบ่อย'],
    'my': ['သွားရောက်လည်ပတ်သူများအတွက်ညွှန်ကြားချက်', 'လူငယ်ကလေးများတွင်တွေ့ရသောရောဂါများ'],
    'km': ['ការណែនាំចំពោះសាច់ញាតិក្នុងពេលទទួលទាន', 'ជំងឺដែលជួបប្រទៈញឹកញាប់នៅក្នុងទារក'],
    'en': ['Guidance for Relatives During Admission', 'Common Neonatal Diseases']
}

# วิดีโอตามภาษา
videos = {
    'th': 'https://www.youtube.com/embed/thai_video_id',
    'my': 'https://www.youtube.com/embed/myanmar_video_id',
    'km': 'https://www.youtube.com/embed/khmer_video_id',
    'en': 'https://www.youtube.com/embed/english_video_id'
}

# รายชื่อโรค
neonatal_diseases = {
    'th': [
        'ความดันเลือดที่ปอดสูง',
        'ทารกคลอดก่อนกำหนด',
        'ภาวะเลือดข้น',
        'ภาวะน้ำตาลในเลือดต่ำ',
        'ภาวะตัวเหลือง'
    ]
    # สามารถเพิ่มภาษาอื่นได้ในภายหลัง
}

@app.route('/')
def index():
    return render_template('index.html', languages=languages)

@app.route('/menu/<lang>')
def menu(lang):
    return render_template('menu.html', lang=lang, topics=main_topics[lang])

@app.route('/video/<lang>')
def video(lang):
    return render_template('video.html', lang=lang, video_url=videos[lang])

@app.route('/diseases/<lang>')
def diseases(lang):
    return render_template('diseases.html', lang=lang, diseases=neonatal_diseases['th'])

if __name__ == '__main__':
    app.run(debug=True)
