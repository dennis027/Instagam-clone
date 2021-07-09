from django.db import models
from django.db.models.deletion import CASCADE
from tinymce.models import HTMLField
# Create your models here.
# class Poster(models.Model):
#     name = models.CharField(max_length=255,primary_key=True)
#     def __str__(self):
#         return self.name
class Likes(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
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
    comment = models.CharField(max_length=255,primary_key=True)
    # poster_id= models.ForeignKey=(Poster)

    def __str__(self):
        return self.comment
class Follower(models.Model) :
    pass       
class Profile(models.Model):
    bio = models.CharField(max_length=100,primary_key=True)
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
    # post=HTMLField()
    # poster=models.ForeignKey('User,on_delete=models.CASCADE')
    caption=models.CharField(max_length=30)
    Profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    Likes = models.ForeignKey(Likes,on_delete=models.CASCADE)
    Comments = models.ForeignKey(Comments,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    @classmethod
    def update_image(cls,id):
        cls.objects.filter(id=id).update(image=object)
