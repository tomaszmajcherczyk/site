"""
Those names at the end of a each path e.g.     path('edit/<int:id>/', edit_post, name='edit_post'),
are necessary to create an anchor in a html file which allow us to e.g. create a button to those urls
"""

from django.urls import path
from .views import img_post_list, new_post, edit_post, delete_post, one_tag

urlpatterns = [
    path('posts/', img_post_list, name='all_posts'),
    path('new/', new_post, name='new_post'),
    path('edit/<int:id>/', edit_post, name='edit_post'),
    path('delete/<int:id>/', delete_post, name='delete_post'),
    path('one_tag/<slug:name>/', one_tag, name='one_tag'),

]