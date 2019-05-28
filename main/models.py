from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser
from django.contrib import admin
# Create your models here.


# class SiteUser(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=200)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return str(self.first_name) + " " + str(self.last_name)

class ImgPostTag(models.Model):
    tag_name = models.SlugField(max_length=50)

    def __str__(self):
        return self.tag_name


class ImgPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # pub_date = models.CharField(max_length=200, null=True, blank=True)
    title = models.TextField(default="post")
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)  # by default django won't display it on admin
    date = models.DateField(default=timezone.now)
    time = models.TimeField(null=True, blank=True, default=timezone.now)
    img_tag = models.ManyToManyField(ImgPostTag, related_name="tags", blank=True)

    def __str__(self):
        return self.title_with_rating()

    def title_with_rating(self):
        return str(self.title) + " (" + str(self.rating) + ")"


