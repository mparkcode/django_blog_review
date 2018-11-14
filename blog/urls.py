from django.urls import path
from blog.views import read_post, edit_post, write_post, get_unpublished_posts



urlpatterns=[
    path('unpublished', get_unpublished_posts, name="get_unpublished_posts"),
    path('read_post/<int:id>', read_post, name="read_post"),
    path('edit_post/<int:id>', edit_post, name="edit_post"),
    path('write_post/', write_post, name="write_post"),
]