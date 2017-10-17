from django.db import models

class Users(models.Model):
     name = models.TextField()
     password = models.TextField()
