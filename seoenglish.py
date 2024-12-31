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

# Set up the font to support Arabic characters (you can replace it with any available font)
matplotlib.rcParams['font.family'] = 'DejaVu Sans'

class SEOAnalysisApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SEO Analysis Tool")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        # Interface components in English
        self.url_label = QLabel('Enter the URL to analyze:')
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText('https://example.com')

        self.analyze_button = QPushButton('Analyze', self)
        self.analyze_button.clicked.connect(self.run_analysis)

        self.result_label = QLabel('Analysis Results:')
        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)

        # Setting up tabs to display results
        self.tabs = QTabWidget()
        self.tabs.addTab(self.result_text, "Results")

        # Save button
        self.save_button = QPushButton('Save Results', self)
        self.save_button.clicked.connect(self.save_results)

        # Layout
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
            return keywords.get('content').split(',') if keywords else "No keywords found."
        except Exception as e:
            return f"Error: {e}"

    def analyze_content_quality(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            headings = soup.find_all(['h1', 'h2', 'h3'])
            content_score = len(headings)
            h1_tags = soup.find_all('h1')
            return f"Content Quality: Number of headings: {content_score}. H1 tags: {len(h1_tags)}."
        except Exception as e:
            return f"Error: {e}"

    def analyze_page_speed(self, url):
        api_key = 'AIzaSyCMkJzrG3RECcqybWzhVCvpX-ZKrQOCWcM'  # Replace this with your API key
        try:
            service = build('pagespeedonline', 'v5', developerKey=api_key)
            result = service.pagespeedapi().runpagespeed(url=url).execute()
            speed_score = result['lighthouseResult']['categories']['performance']['score'] * 100
            performance = result['lighthouseResult']['audits']['speed-index']['displayValue']
            page_size = result['lighthouseResult']['audits']['total-byte-weight']['displayValue']
            return f"Page Speed: {speed_score}%. Performance: {performance}, Page size: {page_size}"
        except Exception as e:
            return f"Error: {e}"

    def analyze_links(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            internal_links = [link['href'] for link in links if link['href'].startswith(url)]
            external_links = [link['href'] for link in links if not link['href'].startswith(url)]
            return f"Internal links: {len(internal_links)}, External links: {len(external_links)}"
        except Exception as e:
            return f"Error: {e}"

    def analyze_robots(self, url):
        try:
            robots_url = f"{url}/robots.txt"
            response = requests.get(robots_url)
            if response.status_code == 200:
                return "robots.txt found."
            else:
                return "robots.txt not found."
        except Exception as e:
            return f"Error: {e}"

    def analyze_images(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            images = soup.find_all('img')
            missing_alt = sum(1 for img in images if not img.get('alt'))
            return f"Images missing 'alt' attribute: {missing_alt} out of {len(images)} images."
        except Exception as e:
            return f"Error: {e}"

    def plot_headings_distribution(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            h1 = len(soup.find_all('h1'))
            h2 = len(soup.find_all('h2'))
            h3 = len(soup.find_all('h3'))
            headings_count = [h1, h2, h3]
            headings_labels = ['H1', 'H2', 'H3']
            
            # Plotting with English labels
            plt.bar(headings_labels, headings_count, color=['blue', 'green', 'orange'])
            plt.title("Headings Distribution on the Page", fontsize=14, family='DejaVu Sans')
            plt.xlabel("Headings", fontsize=12, family='DejaVu Sans')
            plt.ylabel("Number of Headings", fontsize=12, family='DejaVu Sans')
            plt.show()
        except Exception as e:
            return f"Error: {e}"

    def run_analysis(self):
        url = self.url_input.text().strip()
        if not url:
            self.result_text.setText("Please enter a website URL.")
            return

        self.result_text.clear()

        # Extract keywords
        keywords = self.extract_keywords(url)
        self.result_text.append(f"Keywords:\n{keywords}\n")

        # Analyze content quality
        content_quality = self.analyze_content_quality(url)
        self.result_text.append(f"\nContent Quality:\n{content_quality}\n")

        # Analyze page speed
        speed = self.analyze_page_speed(url)
        self.result_text.append(f"\nPage Speed:\n{speed}\n")

        # Analyze links
        links = self.analyze_links(url)
        self.result_text.append(f"\nLinks:\n{links}\n")

        # Analyze robots.txt
        robots = self.analyze_robots(url)
        self.result_text.append(f"\nrobots.txt Analysis:\n{robots}\n")

        # Analyze images
        images = self.analyze_images(url)
        self.result_text.append(f"\nImages:\n{images}\n")

        # Display headings distribution graph
        self.plot_headings_distribution(url)

    def save_results(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Results", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(self.result_text.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SEOAnalysisApp()
    window.show()
    sys.exit(app.exec_())
