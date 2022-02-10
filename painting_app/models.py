from django.db import models

class Painting_Images(models.Model):
    name = models.CharField(max_length=50)
    Main_Img = models.ImageField(upload_to='images/')
