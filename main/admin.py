from django.contrib import admin
from .models import ImgPost, ImgPostTag

# Register your models here.


@admin.register(ImgPost)
class ImgPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'author')  # this being displayed on the /admin


@admin.register(ImgPostTag)
class ImgPostTagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'get_tags')
