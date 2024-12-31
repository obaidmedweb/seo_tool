import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QTabWidget, QFileDialog
from PyQt5.QtCore import Qt
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rcParams
import numpy as np

# تحديد الخطوط العربية
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
# يمكنك استخدام خط آخر إذا كنت قد قمت بتثبيته في النظام مثل 'Amiri' أو 'Tahoma'

class SEOAnalysisApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("أداة تحليل SEO")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        # إعداد الواجهات
        self.url_label = QLabel('أدخل الرابط (URL) لتحليله:')
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText('https://example.com')

        self.analyze_button = QPushButton('تحليل', self)
        self.analyze_button.clicked.connect(self.run_analysis)

        self.result_label = QLabel('نتائج التحليل:')
        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)

        # إعداد التبويبات لعرض النتائج
        self.tabs = QTabWidget()
        self.tabs.addTab(self.result_text, "النتائج")

        # إعداد الأزرار
        self.save_button = QPushButton('حفظ النتائج', self)
        self.save_button.clicked.connect(self.save_results)

        # ترتيب العناصر في واجهة المستخدم
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.url_label)
        v_layout.addWidget(self.url_input)
        v_layout.addWidget(self.analyze_button)
        v_layout.addWidget(self.tabs)
        v_layout.addWidget(self.save_button)

        self.setLayout(v_layout)

    def extract_keywords(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            keywords = soup.find('meta', attrs={'name': 'keywords'})
            return keywords.get('content').split(',') if keywords else "لا توجد كلمات مفتاحية."
        except Exception as e:
            return f"خطأ: {e}"

    def analyze_content_quality(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            headings = soup.find_all(['h1', 'h2', 'h3'])
            content_score = len(headings)
            h1_tags = soup.find_all('h1')
            return f"جودة المحتوى: عدد العناوين: {content_score}. وجود H1: {len(h1_tags)}."
        except Exception as e:
            return f"خطأ: {e}"

    def analyze_page_speed(self, url):
        api_key = 'AIzaSyCMkJzrG3RECcqybWzhVCvpX-ZKrQOCWcM'  # استبدل هذا بمفتاح API الخاص بك
        try:
            service = build('pagespeedonline', 'v5', developerKey=api_key)
            result = service.pagespeedapi().runpagespeed(url=url).execute()
            speed_score = result['lighthouseResult']['categories']['performance']['score'] * 100
            performance = result['lighthouseResult']['audits']['speed-index']['displayValue']
            page_size = result['lighthouseResult']['audits']['total-byte-weight']['displayValue']
            return f"سرعة تحميل الصفحة: {speed_score}%. أداء التحميل: {performance}, حجم الصفحة: {page_size}"
        except Exception as e:
            return f"خطأ: {e}"

    def analyze_links(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            internal_links = [link['href'] for link in links if link['href'].startswith(url)]
            external_links = [link['href'] for link in links if not link['href'].startswith(url)]
            return f"عدد الروابط الداخلية: {len(internal_links)}, عدد الروابط الخارجية: {len(external_links)}"
        except Exception as e:
            return f"خطأ: {e}"

    def analyze_robots(self, url):
        try:
            robots_url = f"{url}/robots.txt"
            response = requests.get(robots_url)
            if response.status_code == 200:
                return "الـ robots.txt موجود."
            else:
                return "الـ robots.txt غير موجود."
        except Exception as e:
            return f"خطأ: {e}"

    def analyze_images(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            images = soup.find_all('img')
            missing_alt = sum(1 for img in images if not img.get('alt'))
            return f"عدد الصور التي تفتقر إلى 'alt' tag: {missing_alt} من أصل {len(images)} صورة."
        except Exception as e:
            return f"خطأ: {e}"

    def plot_headings_distribution(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            h1 = len(soup.find_all('h1'))
            h2 = len(soup.find_all('h2'))
            h3 = len(soup.find_all('h3'))
            headings_count = [h1, h2, h3]
            headings_labels = ['H1', 'H2', 'H3']
            
            # رسم بياني مع دعم اللغة العربية
            plt.bar(headings_labels, headings_count, color=['blue', 'green', 'orange'])
            plt.title("توزيع العناوين في الصفحة", fontsize=14, family='DejaVu Sans')
            plt.xlabel("العناوين", fontsize=12, family='DejaVu Sans')
            plt.ylabel("عدد العناوين", fontsize=12, family='DejaVu Sans')
            plt.show()
        except Exception as e:
            return f"خطأ: {e}"

    def run_analysis(self):
        url = self.url_input.text().strip()
        if not url:
            self.result_text.setText("يرجى إدخال رابط الموقع.")
            return

        self.result_text.clear()

        # تحليل الكلمات المفتاحية
        keywords = self.extract_keywords(url)
        self.result_text.append(f"الكلمات المفتاحية:\n{keywords}\n")

        # تحليل جودة المحتوى
        content_quality = self.analyze_content_quality(url)
        self.result_text.append(f"\nجودة المحتوى:\n{content_quality}\n")

        # تحليل سرعة الصفحة
        speed = self.analyze_page_speed(url)
        self.result_text.append(f"\nسرعة تحميل الصفحة:\n{speed}\n")

        # تحليل الروابط
        links = self.analyze_links(url)
        self.result_text.append(f"\nالروابط:\n{links}\n")

        # تحليل الـ robots.txt
        robots = self.analyze_robots(url)
        self.result_text.append(f"\nتحليل robots.txt:\n{robots}\n")

        # تحليل الصور
        images = self.analyze_images(url)
        self.result_text.append(f"\nالصور:\n{images}\n")

        # عرض الرسم البياني لتوزيع العناوين
        self.plot_headings_distribution(url)

    def save_results(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "حفظ النتائج", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(self.result_text.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SEOAnalysisApp()
    window.show()
    sys.exit(app.exec_())
