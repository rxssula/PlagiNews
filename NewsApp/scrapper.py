from .models import NewsItem, SportItem, EduItem
from bs4 import BeautifulSoup
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
            new_link = original_link + new.a.picture.source['srcset']
            image_link = new_link
            title = new.find('span', class_='content_main_item_title').a.text
            text = new.find('span', class_='content_main_item_announce').text
            b = NewsItem(title=title, image_link=image_link, link=link, description=text)
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
            new_link = original_link + new.a.picture.source['srcset']
            image_link = new_link
            title = new.find('span', class_='content_main_item_title').a.text
            text = new.find('span', class_='content_main_item_announce').text
            b = SportItem(title=title, image_link=image_link, link=link, description=text)
            if SportItem.objects.filter(title = title).exists():
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
            new_link = original_link + new.a.picture.source['srcset']
            image_link = new_link
            title = new.find('span', class_='content_main_item_title').a.text
            text = new.find('span', class_='content_main_item_announce').text
            b = EduItem(title=title, image_link=image_link, link=link, description=text)
            if EduItem.objects.filter(title = title).exists():
                continue
            else:
                b.save()