"""
URL configuration for notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from base.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("note_type/", note_type, name="note_type"),
    path("create_note/", create_note, name="create_note"),
    path("create_notetype/", create_notetype, name="create_notetype"),
    path("edit_note/<int:pk>/", edit_note, name="edit_note"),
    path("delete_note/<int:pk>", delete_note, name="delete_note"),
    path("delete_all_note/", delete_all_note, name="delete_all_note")
]
