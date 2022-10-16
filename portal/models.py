from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    author_name = models.CharField(max_length=300,null=True)
    title = models.CharField(max_length=500,null=True)
    slug = models.CharField(max_length=200,null=True)
    image=models.ImageField(("image"),upload_to='portal/image',null=True)
    description = RichTextField(blank=True,null=True)
    posted_on = models.DateTimeField(auto_now_add=True, blank=True)