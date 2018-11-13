"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import index, read_post, edit_post, write_post, get_unpublished_posts
from accounts.views import signup
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup, name="signup"),
    path('', index, name="index"),
    path('posts/unpublished', get_unpublished_posts, name="get_unpublished_posts"),
    path('posts/read_post/<int:id>', read_post, name="read_post"),
    path('posts/edit_post/<int:id>', edit_post, name="edit_post"),
    path('posts/write_post/', write_post, name="write_post"),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
