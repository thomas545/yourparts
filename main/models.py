from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Weather(models.Model):
    city = models.CharField(max_length=200)


    def __str__(self):
        return '%s' % (self.city)