from django.db import models

# Create your models here.
class mosquito(models.Model):
  created= models.DateTimeField(auto_now_add=True)
  city=models.CharField(max_length=122)
  mosquito = models.CharField(max_length=30)
