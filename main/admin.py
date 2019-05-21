from django.contrib import admin
from .models import ImgPost, SiteUser

# Register your models here.


@admin.register(ImgPost)
class ImgPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'pub_date')  # this being displayed on the /admin


@admin.register(SiteUser)
class SiteUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_active')
