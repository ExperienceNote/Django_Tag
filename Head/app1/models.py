from django.db import models

class Data_(models.Model):
    ORGANISATION = models.CharField(max_length=200)
    PRODUCT= models.CharField(max_length=200)
    DATE= models.CharField(max_length=20)
    EVENT= models.CharField(max_length=200)
    TIME= models.CharField(max_length=200)
    LOCATION= models.CharField(max_length=200)
    PERSON= models.CharField(max_length=200)
    GPE= models.CharField(max_length=200)
