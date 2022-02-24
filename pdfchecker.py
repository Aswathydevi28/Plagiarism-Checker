import requests
from bs4 import BeautifulSoup
import io
from PyPDF2 import PdfFileReader

url = "https://www.rgpvonline.com/rgpv-first-year.html"
read = requests.get(url)
html_content = read.content
soup = BeautifulSoup(html_content,"html.parser")

list_of_pdf = set()
l = soup.find('p')
p = l.find_all('a')

for link in (p):
    pdf_link = (link.get('href')[:-5]) + ".pdf"
    print(pdf_link)
    list_of_pdf.add(pdf_link)

