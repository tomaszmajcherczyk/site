from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

from django.contrib import admin
# Create your models here.


class ImgPostTag(models.Model):
    tag_name = models.SlugField(max_length=50)

    def __str__(self):
        return self.tag_name


class ImgPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(default="post")
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)  # by default django won't
    # display it on admin
    date = models.DateField(default=timezone.now)
    time = models.TimeField(null=True, blank=True, default=timezone.now)
    img_tags = models.ManyToManyField(ImgPostTag, related_name="tags", blank=True)  # to display is on the site I needed
    # to add an

    def __str__(self):
        return f"{self.title_with_rating()}"

    def title_with_rating(self):
        return f"{self.title} ({self.rating})"

    def tag_display(self):
        return ", ".join([str(tag) for tag in self.img_tags.all()])
