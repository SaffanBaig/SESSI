from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=200)
    files=models.FileField(upload_to='ads/files/')

    def __str__(self):
        return self.title
