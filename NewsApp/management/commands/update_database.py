from django.core.management.base import BaseCommand
from NewsApp.scrapper import scrap_news, scrap_edu, scrap_sport
from NewsApp.models import NewsItem, SportItem, EduItem
import schedule
import time

class Command(BaseCommand):
    help = 'Updates the database'

    def handle(self, *args, **options):

        def run_update_command():
            scrap_sport()
            scrap_edu()
            scrap_news()
            print('Updated database')

        schedule.every().minute.do(run_update_command)

        while True:
            schedule.run_pending()
            time.sleep(1)
