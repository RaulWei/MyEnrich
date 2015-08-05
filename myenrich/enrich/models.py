from django.db import models
from django.contrib import admin

# Create your models here.

class Milestone(models.Model):
    Content = models.CharField(max_length=500)
    Date = models.CharField(max_length=200)

admin.site.register(Milestone)
