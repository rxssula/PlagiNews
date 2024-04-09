from django.db import models

class SportItem(models.Model):
    title = models.CharField(max_length=200)
    image_link = models.URLField()
    link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title

class EduItem(models.Model):
    title = models.CharField(max_length=200)
    image_link = models.URLField()
    link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title
# Create your models here.
class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    image_link = models.URLField()
    link = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title