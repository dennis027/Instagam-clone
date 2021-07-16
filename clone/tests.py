from django.test import TestCase
from models import *
from django.core.files.uploadedfile import SimpleFileUpload


# Create your tests here.

class ImageTestCase(TestCase):
    def setUp(self):
        self.new = Image(name='new', caption='smart')

    
    def test_instances(self):
        self.assertTrue(isinstance(self.new,Image))    

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'MEDIA/test.jpg')
        changed_img = Image.objects.filter(image='MEDIA/test.jpg')
        self.assertTrue(len(changed_img) > 0)

class PosterTestClass(TestCase):
    def setUp(self):
        self.kimani= Poster(first_name ='kimani', last_name='dennis',email='kimani@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.kimani, Poster))

    def test_save_method(self):
        self.kimani.save_poster()
        posters = Poster.objects.all()
        self.assertTrue(len(posters)>0)

    def test_delete_method(self):
        self.kimani.save_poster()
        poster = Poster.objects.all()
        self.kimani.delete_poster()
        self.assertTrue(len(poster)==0)    