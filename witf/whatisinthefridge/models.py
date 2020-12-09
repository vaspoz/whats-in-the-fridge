from django.db import models


class Food(models.Model):
    label = models.CharField(max_length=250)

