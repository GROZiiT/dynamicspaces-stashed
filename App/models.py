from django.db import models
import time
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.
class Jobs(models.Model):
    title= models.CharField(max_length=500)
    keywords=models.CharField(max_length=500)
    company=models.CharField(max_length=500,default="")
    sdescription=models.CharField(max_length=500)
    description=RichTextField()
    background_img_url = models.CharField(max_length=500)
    logo_img_url = models.CharField(max_length=500)
    location=models.CharField(max_length=500)
    eemail = models.CharField(max_length=500)
    expire_in_days=models.DateField()
    time=models.DateField(editable=False,default=datetime.now())
    posted_by=models.CharField(max_length=500)

class Profiles(models.Model):
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500,unique=True)
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    comapny = models.CharField(max_length=500)
    job = models.CharField(max_length=500)
    email_verfied = models.BooleanField(default=False)
    subscriber = models.BooleanField(default=False)
    subscriber_id = models.CharField(max_length=500,default="")
    key = models.CharField(max_length=500)
    img_url = models.CharField(max_length=500)
    profile_pic = models.ImageField(upload_to='images')