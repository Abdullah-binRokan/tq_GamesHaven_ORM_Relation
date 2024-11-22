from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField()
    image = models.ImageField(upload_to="publishers_images/", default="publishers_images/default.jpg")