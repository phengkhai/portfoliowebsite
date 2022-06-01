# Create your models here.
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name="name")
    parent = models.ForeignKey('self',blank=True, on_delete = models.CASCADE, null=True ,related_name='children')
    slug = models.SlugField(unique=True, max_length=130)
    def __str__(self):
        return self.name

    def get_article(self):
        return Projects.objects.filter(category=self)

class Projects(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    desc = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT,blank=True,null=True)
    slug = models.SlugField(unique=True, max_length = 130)
    def __str__(self):
        return self.title

    def get_unique_slug(self):
        slug = slugify(self.title.replace("ı","i"))
        unique_slug = slug
        counter = 1
        while Projects.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_unique_slug()
        return super(Projects, self).save(*args, **kwargs)