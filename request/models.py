from django.db import models

class Rerust(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    question = models.TextField()