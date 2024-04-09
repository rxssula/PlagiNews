from django.contrib import admin
from .models import NewsItem, SportItem, EduItem

# Register your models here.
admin.site.register(NewsItem)
admin.site.register(EduItem)
admin.site.register(SportItem)
