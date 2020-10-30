from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Image(models.Model):
    title = models.CharField(max_length=180)
    description = models.TextField(max_length=1180)
    image = CloudinaryField('image')
    content  = models.TextField(max_length=1180)
    author = models.CharField(max_length=180)
    Published = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





    