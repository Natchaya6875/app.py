<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Newborn Info</title>
  <style>
    body {
      font-family: sans-serif;
      padding: 20px;
      text-align: center;
    }
    .flag {
      width: 40px;
      height: 25px;
      vertical-align: middle;
    }
    .language-button, .topic-button, .disease-button {
      display: block;
      margin: 10px auto;
      padding: 10px;
      width: 300px;
      font-size: 16px;
    }
    .hidden {
      display: none;
    }
  </style>
</head>
<body>
  <!-- Page 1: Language Selection -->
  <div id="page1">
    <h2>กรุณาเลือกภาษา / Please select a language</h2>
    <button class="language-button" onclick="selectLanguage('th')">
      <img src="https://flagcdn.com/th.svg" class="flag"> ภาษาไทย
    </button>
    <button class="language-button" onclick="selectLanguage('my')">
      <img src="https://flagcdn.com/mm.svg" class="flag"> မြန်မာစာ
    </button>
    <button class="language-button" onclick="selectLanguage('km')">
      <img src="https://flagcdn.com/kh.svg" class="flag"> ភាសាខ្មែរ
    </button>
    <button class="language-button" onclick="selectLanguage('en')">
      <img src="https://flagcdn.com/gb.svg" class="flag"> English
    </button>
  </div>

  <!-- Page 2: Main Topics -->
  <div id="page2" class="hidden">
    <h2 id="mainTitle"></h2>
    <button class="topic-button" onclick="watchVideo()" id="topic1"></button>
    <button class="topic-button" onclick="goToDiseasesPage()" id="topic2"></button>
  </div>

  <!-- Page 4: Disease List -->
  <div id="page4" class="hidden">
    <h2 id="diseaseTitle"></h2>
    <ul id="diseaseList"></ul>
    <button onclick="goBackToTopics()">← กลับ / Back</button>
  </div>

  <script>
    const content = {
      th: {
        mainTitle: "กรุณาเลือกหัวข้อ",
        topic1: "การแนะนำการปฏิบัติตัวแก่ญาติขณะรับใหม่",
        topic2: "โรคต่างๆในทารกแรกเกิดที่พบบ่อย",
        videoUrl: "https://example.com/th_video.mp4",
        diseaseTitle: "โรคต่างๆในทารกแรกเกิดที่พบบ่อย",
        diseases: ["ความดันเลือดที่ปอดสูง", "ทารกคลอดก่อนกำหนด", "ภาวะเลือดข้น", "ภาวะน้ำตาลในเลือดต่ำ", "ภาวะตัวเหลือง"]
      },
      my: {
        mainTitle: "ခင်ဗျား ရွေးချယ်ရန်ခေါင်းစဉ်",
        topic1: "လက်ခံနေစဉ်တွင်မိသားစုများအတွက်လမ်းညွှန်ချက်",
        topic2: "လူနာကလေးငယ်များတွင်တွေ့ရသောရောဂါများ",
        videoUrl: "https://example.com/my_video.mp4",
        diseaseTitle: "လူနာကလေးငယ်များတွင်တွေ့ရသောရောဂါများ",
        diseases: ["အဆုတ်သွေးဖိအားမြင့်", "မချိန်မှီမွေးဖွားခြင်း", "အရောင်ရောင်သွေးများခြင်း", "သွေးရှူခါနီး", "အဝါရောင်ဖြစ်ခြင်း"]
      },
      km: {
        mainTitle: "សូមជ្រើសរើសប្រធានបទ",
        topic1: "ការណែនាំសម្រាប់គ្រួសារពេលទទួលទារក",
        topic2: "ជំងឺទូទៅនៅក្នុងទារកកើតថ្មី",
        videoUrl: "https://example.com/km_video.mp4",
        diseaseTitle: "ជំងឺទូទៅនៅក្នុងទារកកើតថ្មី",
        diseases: ["សម្ពាធឈាមខ្ពស់នៅសួត", "ការបង្កើតមុនកំណត់", "ឈាមខាត់ខ្ទង់", "ស្ករឈាមទាប", "ចោលខាងក្រៅ"]
      },
      en: {
        mainTitle: "Please choose a topic",
        topic1: "Instructions for Relatives upon Admission",
        topic2: "Common Neonatal Conditions",
        videoUrl: "https://example.com/en_video.mp4",
        diseaseTitle: "Common Neonatal Conditions",
        diseases: ["Pulmonary Hypertension", "Prematurity", "Polycythemia", "Hypoglycemia", "Jaundice"]
      }
    };

    let selectedLang = 'th';

    function selectLanguage(lang) {
      selectedLang = lang;
      document.getElementById('page1').classList.add('hidden');
      document.getElementById('page2').classList.remove('hidden');

      const langContent = content[lang];
      document.getElementById('mainTitle').innerText = langContent.mainTitle;
      document.getElementById('topic1').innerText = langContent.topic1;
      document.getElementById('topic2').innerText = langContent.topic2;
    }

    function watchVideo() {
      const videoUrl = content[selectedLang].videoUrl;
      window.open(videoUrl, '_blank');
      setTimeout(() => {
        document.getElementById('page2').classList.remove('hidden');
      }, 1000);
    }

    function goToDiseasesPage() {
      const langContent = content[selectedLang];
      document.getElementById('page2').classList.add('hidden');
      document.getElementById('page4').classList.remove('hidden');

      document.getElementById('diseaseTitle').innerText = langContent.diseaseTitle;
      const diseaseList = document.getElementById('diseaseList');
      diseaseList.innerHTML = '';
      langContent.diseases.forEach(disease => {
        const li = document.createElement('li');
        li.innerText = disease;
        diseaseList.appendChild(li);
      });
    }

    function goBackToTopics() {
      document.getElementById('page4').classList.add('hidden');
      document.getElementById('page2').classList.remove('hidden');
    }
  </script>
</body>
</html>
