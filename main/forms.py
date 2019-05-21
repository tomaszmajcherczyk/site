from django.forms import ModelForm
from .models import ImgPost


#  from this class we're able to create a movie on a site but not /admin, /new in this case
class ImgPostForm(ModelForm):
    class Meta:
        model = ImgPost
        fields = ['title', 'rating', 'photo', 'pub_date']
