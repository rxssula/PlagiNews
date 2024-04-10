from .models import NewsItem
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests

def scrap_news():
    for i in range(1, 6):
        original_link = 'https://tengrinews.kz'
        html_text = requests.get('https://tengrinews.kz/news/page/' + str(i) + '/').text
        soup = BeautifulSoup(html_text, 'lxml')
        news = soup.find_all('div', class_='content_main_item')
        for new in news:
            new_link = original_link + new.a['href']
            link = new_link
            # html_text = requests.get(link).text
            # soup = BeautifulSoup(html_text, 'lxml')
            # time = soup.find('div', class_='date-time').text
            new_link = original_link + new.a.picture.source['srcset']
            image_link = new_link
            title = new.find('span', class_='content_main_item_title').a.text
            text = new.find('span', class_='content_main_item_announce').text
            b = NewsItem(title=title, image_link=image_link, link=link, description=text, category='news', date=datetime.now())
            if NewsItem.objects.filter(title = title).exists():
                continue
            else:
                b.save()
def scrap_sport():
    for i in range(1, 6):
        original_link = 'https://tengrisport.kz'
        html_text = requests.get('https://tengrisport.kz/tnsport/page/' + str(i) + '/').text
        soup = BeautifulSoup(html_text, 'lxml')
        news = soup.find_all('div', class_='content_main_item')
        for new in news:
            new_link = new.a['href']
            link = new_link
            # html_text = requests.get(link).text
            # soup = BeautifulSoup(html_text, 'lxml')
            # time = soup.find('div', class_='date-time').text
            # if 'Вчера' in time:
            #     today = datetime.today()
            #     time = today - timedelta(days=1)
            new_link = original_link + new.a.picture.source['srcset']
            image_link = new_link
            title = new.find('span', class_='content_main_item_title').a.text
            text = new.find('span', class_='content_main_item_announce').text
            b = NewsItem(title=title, image_link=image_link, link=link, description=text, category='sport', date=datetime.now())
            if NewsItem.objects.filter(title = title).exists():
                continue
            else:
                b.save()
def scrap_edu():
    for i in range(1, 6):
        original_link = 'https://tengrinews.kz'
        html_text = requests.get('https://tengrinews.kz/newseducation/page/' + str(i) + '/').text
        soup = BeautifulSoup(html_text, 'lxml')
        news = soup.find_all('div', class_='content_main_item')
        for new in news:
            new_link = original_link + new.a['href']
            link = new_link
            # html_text = requests.get(link).text
            # soup = BeautifulSoup(html_text, 'lxml')
            # time = soup.find('div', class_='date-time').text
            new_link = original_link + new.a.picture.source['srcset']
            image_link = new_link
            title = new.find('span', class_='content_main_item_title').a.text
            text = new.find('span', class_='content_main_item_announce').text
            b = NewsItem(title=title, image_link=image_link, link=link, description=text, category='edu', date=datetime.now())
            if NewsItem.objects.filter(title = title).exists():
                continue
            else:
                b.save()