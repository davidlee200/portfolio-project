from django.db import models


class Job(models.Model):
    imgane = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
