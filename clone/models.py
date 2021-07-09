from django.db import models

# Create your models here.
class Likes(models.Model):
    name = models.CharField(max_length=30)


class Comments(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Profile(models.Model):
    bio = models.CharField(max_length=100)
    Profile_photo= models.ImageField(upload_to='MEDIA/')

    def __str__(self):
        return self.bio

class Image(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='MEDIA/')
    caption=models.CharField(max_length=30)
    Profile=models.ForeignKey(Profile)
    Likes = models.ForeignKey(Likes)
    Comments = models.ForeignKey(Comments)
    def __str__(self):
        return self.name

