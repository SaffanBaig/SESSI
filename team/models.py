from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name

class Seniority(models.Model):
    title = models.CharField(max_length=200)
    files = models.FileField(upload_to='files/')
    def __str__(self):
        return self.title