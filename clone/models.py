from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='MEDIA/')
    pass
class Likes(models.Model):
    pass
class Comments(models.Model):
    pass
class Profile(models.Model):
    pass
