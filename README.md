### **دليل المستخدم (README.md)**

# أداة تحليل SEO (SEO Analysis Tool)

#### **الوصف (Description):**
أداة تحليل SEO هي أداة قوية لتحليل المواقع الإلكترونية من حيث تحسين محركات البحث (SEO). تمكنك هذه الأداة من تحليل عدة جوانب للموقع مثل الكلمات المفتاحية، جودة المحتوى، سرعة التحميل، الروابط، والعديد من التحليلات الأخرى.

تم تطوير هذه الأداة باستخدام بايثون مع واجهة مستخدم رسومية (GUI) باستخدام مكتبة PyQt5، مما يتيح لك التفاعل مع الأداة بشكل سهل ومريح.

---

### **المتطلبات (Requirements):**

- Python 3.x
- المكتبات التالية:
  - `requests`
  - `beautifulsoup4`
  - `google-api-python-client`
  - `PyQt5`
  - `matplotlib`

---

### **التثبيت (Installation):**

1. قم بتثبيت بايثون (إن لم يكن مثبتاً على جهازك).
2. قم بإنشاء بيئة افتراضية (اختياري):
   ```bash
   python -m venv venv
   source venv/bin/activate  # على macOS/Linux
   venv\Scripts\activate     # على Windows
   ```
3. قم بتثبيت المكتبات المطلوبة:
   ```bash
   pip install requests beautifulsoup4 google-api-python-client PyQt5 matplotlib
   ```

---

### **كيفية الاستخدام (Usage):**

1. قم بتشغيل البرنامج باستخدام الأمر التالي:
   ```bash
   python seo_tool.py
   ```
   أو بالواجهة الانجليزية
   ```bash
   python seoenglish.py
   ```


2. بعد تشغيل الأداة، يمكنك إدخال الرابط (URL) الخاص بالموقع الذي ترغب في تحليله في الخانة المخصصة.
3. اضغط على زر "تحليل" لتحصل على تحليل SEO للموقع.
4. يمكنك حفظ النتائج في ملف نصي عبر زر "حفظ النتائج".
5. سيتم عرض نتائج التحليل في واجهة المستخدم مع رسوم بيانية توضح توزيع العناوين في الصفحة.

---

### **المميزات (Features):**
- تحليل الكلمات المفتاحية (Keywords).
- تحليل جودة المحتوى (Content Quality).
- تحليل سرعة تحميل الصفحة (Page Speed).
- تحليل الروابط الداخلية والخارجية (Links).
- تحليل ملف robots.txt.
- تحليل الصور المفقودة "alt" (Missing alt in images).
- عرض رسم بياني لتوزيع العناوين H1, H2, H3.

---

### **ملاحظات (Notes):**

- تأكد من استبدال مفتاح API الخاص بك من **Google PageSpeed Insights** في الكود.
- يمكنك حفظ النتائج كملف نصي باستخدام خيار "حفظ النتائج".

---

### **المساهمة (Contributing):**

إذا كنت ترغب في المساهمة في تحسين الأداة، يمكنك اتباع الخطوات التالية:

1. قم بعمل Fork لهذا المستودع.
2. أنشئ فرعًا جديدًا (Branch) لإجراء التعديلات.
3. قم بإجراء التعديلات اللازمة.
4. قدم Pull Request للمراجعة.

---

### **ترخيص (License):**

تم تطوير هذه الأداة بموجب ترخيص مفتوح المصدر. يمكنك استخدامها وتعديلها وفقًا لشروط الترخيص.

---

## **English Version (English README)**

### **Title:**
# SEO Analysis Tool

### **Description:**
The SEO Analysis Tool is a powerful tool for analyzing websites in terms of SEO (Search Engine Optimization). This tool allows you to analyze various aspects of a website, such as keywords, content quality, page speed, links, and many other SEO-related metrics.

This tool is developed using Python with a graphical user interface (GUI) using the PyQt5 library, providing an easy and user-friendly way to interact with the tool.

---

### **Requirements:**

- Python 3.x
- The following libraries:
  - `requests`
  - `beautifulsoup4`
  - `google-api-python-client`
  - `PyQt5`
  - `matplotlib`

---

### **Installation:**

1. Install Python (if not already installed).
2. Create a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # on macOS/Linux
   venv\Scripts\activate     # on Windows
   ```
3. Install the required libraries:
   ```bash
   pip install requests beautifulsoup4 google-api-python-client PyQt5 matplotlib

   ```

---

### **Usage:**

1. Run the application with the following command: 
   Arabic interface:
   ```bash
   python seotool.py
   ```
   English Interface:
      ```bash
   python seoenglish.py
   ```

3. Once the tool is running, enter the URL of the website you want to analyze in the provided field.
4. Press the "Analyze" button to get the SEO analysis for the website.
5. You can save the results to a text file by clicking the "Save Results" button.
6. The analysis results will be displayed in the UI, including graphical charts showing the distribution of headings on the page.

---

### **Features:**
- Keyword analysis.
- Content quality analysis.
- Page speed analysis.
- Internal and external link analysis.
- robots.txt file analysis.
- Missing alt attribute analysis for images.
- Graphical chart displaying H1, H2, H3 heading distribution.

---

### **Notes:**

- Be sure to replace the API key with your own from **Google PageSpeed Insights** in the code.
- You can save the analysis results as a text file using the "Save Results" button.

---

### **Contributing:**

If you would like to contribute to improving the tool, follow these steps:

1. Fork this repository.
2. Create a new branch for your changes.
3. Make the necessary changes.
4. Submit a Pull Request for review.

---

### **License:**

This tool is developed under an open-source license. You are free to use and modify it according to the terms of the license.

---

بهذا الشكل، تم توفير دليل المستخدم بشكل كامل باللغة العربية والإنجليزية.
