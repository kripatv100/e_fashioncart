from django.db import models

# Create your models here.
class SiteSetting(models.Model):
   banner_image=models.ImageField(upload_to='media/',null=True) 
   caption=models.TextField