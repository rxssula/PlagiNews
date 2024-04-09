# from .models import NewsItem, SportItem, EduItem
from django.core.paginator import Paginator
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.

def edu(request):
    original_link = 'https://tengrinews.kz'
    html_text = requests.get('https://tengrinews.kz/newseducation/').text
    soup = BeautifulSoup(html_text, 'lxml')
    news = soup.find_all('div', class_='content_main_item')

    title = []
    link = []
    image_link = []
    text = []
    for new in news:
        new_link = original_link + new.a['href']
        link.append(new_link)
        new_link = original_link + new.a.picture.source['srcset']
        image_link.append(new_link)
        title.append(new.find('span', class_='content_main_item_title').a.text)
        text.append(new.find('span', class_='content_main_item_announce').text)
    news = zip(link, image_link, title, text)
    return render(request, 'NewsApp/edu.html', {'news': news})

def sport(request):
    original_link = 'https://tengrisport.kz'
    html_text = requests.get('https://tengrisport.kz/tnsport/').text
    soup = BeautifulSoup(html_text, 'lxml')
    news = soup.find_all('div', class_='content_main_item')

    title = []
    link = []
    image_link = []
    text = []
    for new in news:
        new_link = new.a['href']
        link.append(new_link)
        new_link = original_link + new.a.picture.source['srcset']
        image_link.append(new_link)
        title.append(new.find('span', class_='content_main_item_title').a.text)
        text.append(new.find('span', class_='content_main_item_announce').text)
    news = zip(link, image_link, title, text)
    return render(request, 'NewsApp/sport.html', {'news': news})
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        original_link = 'https://tengrinews.kz'
        html_text = requests.get('https://tengrinews.kz/search/?text=' + searched).text
        soup = BeautifulSoup(html_text, 'lxml')
        news = soup.find_all('div', class_='content_main_item')

        title = []
        link = []
        image_link = []
        text = []
        for new in news:
            new_link = ''
            if new.a['href'][:5] == 'https':
                new_link = new.a['href']
            else:
                new_link = original_link + new.a['href']
            link.append(new_link)
            new_link = new.a.picture.source['srcset']
            image_link.append(new_link)
            title.append(new.find('span', class_='content_main_item_title').a.text)
            text.append(new.find('span', class_='content_main_item_announce').text)
        news = zip(link, image_link, title, text)
        return render(request, 'NewsApp/search.html', {'searched': searched, 'news': news})
    else:
        return render(request, 'NewsApp/search.html', {})
def index(request):
    original_link = 'https://tengrinews.kz'
    html_text = requests.get('https://tengrinews.kz/news/page/1/').text
    soup = BeautifulSoup(html_text, 'lxml')
    news = soup.find_all('div', class_='content_main_item')

    title = []
    link = []
    image_link = []
    text = []
    for new in news:
        new_link = original_link + new.a['href']
        link.append(new_link)
        new_link = original_link + new.a.picture.source['srcset']
        image_link.append(new_link)
        title.append(new.find('span', class_='content_main_item_title').a.text)
        text.append(new.find('span', class_='content_main_item_announce').text)
    news = zip(link, image_link, title, text)
    return render(request, 'NewsApp/index.html', {'news': news})
