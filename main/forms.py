from django.forms import ModelForm
from .models import ImgPost, ImgPostTag
from django import forms


#  from this class we're able to create a movie on a site but not /admin, /new in this case
class ImgPostForm(ModelForm):
    class Meta:
        model = ImgPost
        fields = ['title', 'rating', 'photo', 'author']
        widgets = {'author': forms.HiddenInput()}  # make the author field hidden, but only on the /new/posts it's still
        # visible on admin


class ImgPostTagForm(ModelForm):
    class Meta:
        model = ImgPostTag
        fields = ['tag_name', 'img_tag']
