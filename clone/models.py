from django.db import models
from django.db.models.deletion import CASCADE
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Poster(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    def __str__(self):
        return self.name
class Likes(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    def save_like(self):
        self.save()
    def delete_like(self):
        self.delete()
    @classmethod
    def update_like(cls,id):
        cls.objects.filter(id=id).update(like=object)    

class Comments(models.Model):
    comment = models.CharField(max_length=255)
    poster= models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
class Follower(models.Model) :
    username = models.CharField(blank=True,max_length = 255)
    followed = models.CharField(blank=True,max_length = 255)

    def __str__(self):
        return f'{self.username}'
     
class Profile(models.Model):
    bio = models.CharField(max_length=100)
    Profile_photo= models.ImageField(upload_to='MEDIA/')

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
    @classmethod
    def update_profile(cls,id):
        cls.objects.filter(id=id).update(profile=object)    

class Image(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    image = models.ImageField(upload_to='MEDIA/')
    post=HTMLField()
    poster= models.ForeignKey(User,on_delete=models.CASCADE)
    caption=models.CharField(max_length=30)
    # created_date = models.DateTimeField(default=timezone.now)
    profile_id=models.ForeignKey(User,related_name='profile',on_delete=models.CASCADE)
    likes_id = models.ForeignKey(User,related_name='likes',on_delete=models.CASCADE)
    comments_id = models.ForeignKey(User,related_name='comment',on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    @classmethod
    def update_image(cls,id):
        cls.objects.filter(id=id).update(image=object)
