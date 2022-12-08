from django.db import models

# Create your models here.

# Question Response Model
class Response(models.Model):
    question = models.CharField(max_length= 100)

    def __str__(self):
        return str(self.name)