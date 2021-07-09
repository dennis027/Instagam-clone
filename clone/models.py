from django.db import models

# Create your models here.
class Likes(models.Model):
    name = models.CharField(max_length=30)

    
class Comments(models.Model):
    pass
class Profile(models.Model):
    pass
class Image(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='MEDIA/')
    caption=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

