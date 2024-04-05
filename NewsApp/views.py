from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.

def search(request):
    return render(request, 'NewsApp/search.html', {})
def index(request):
    original_link = 'https://tengrinews.kz'
    html_text = requests.get('https://tengrinews.kz/news/page/1/').text
    soup = BeautifulSoup(html_text, 'lxml')
    news = soup.find_all('div', class_='content_main_item')

    title = []
    link = []
    image_link = []
    for new in news:
        new_link = original_link + new.a['href']
        link.append(new_link)
        new_link = original_link + new.a.picture.source['srcset']
        image_link.append(new_link)
        title.append(new.find('span', class_='content_main_item_title').a.text)
    news = zip(link, image_link, title)
    return render(request, 'newsapp/index.html', {'news': news})
