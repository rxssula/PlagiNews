from .models import NewsItem
from django.core.paginator import Paginator
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.

def edu(request):
    # scrap_edu()
    p = Paginator(NewsItem.objects.all().filter(category='edu').order_by('-date'), 21)
    page = request.GET.get('page')
    news_list = p.get_page(page)
    nums = 'a' * news_list.paginator.num_pages
    return render(request, 'NewsApp/edu.html', {'nums': nums, 'news_list': news_list})

def sport(request):
    # scrap_sport()
    p = Paginator(NewsItem.objects.all().filter(category='sport').order_by('-date'), 21)
    page = request.GET.get('page')
    news_list = p.get_page(page)
    nums = 'a' * news_list.paginator.num_pages
    return render(request, 'NewsApp/sport.html', {'news_list': news_list, 'nums': nums})
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
    # scrap_news()
    p = Paginator(NewsItem.objects.all().filter(category='news').order_by('-date'), 21)
    page = request.GET.get('page')
    news_list = p.get_page(page)
    nums = 'a' * news_list.paginator.num_pages
    return render(request, 'NewsApp/index.html', {'nums': nums, 'news_list': news_list})
