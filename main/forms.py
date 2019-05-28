from django.forms import ModelForm
from .models import ImgPost, ImgPostTag
from django import forms


#  from this class we're able to add a movie on a site but not /admin, /new in this case  this ImgPostFrom is defined
#  views as "form"
class ImgPostForm(ModelForm):
    class Meta:
        model = ImgPost
        fields = ['title', 'rating', 'photo', 'author', 'img_tag']
        widgets = {'author': forms.HiddenInput()}  # make the author field hidden, but only on the /new/posts it's still
        # visible on admin


