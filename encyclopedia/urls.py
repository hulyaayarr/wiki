from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("searching/", views.searching, name='searching'),
    path("new/", views.new,name="new"),
    path("wiki/<str:title>/" ,views.entry_title, name="entry_title"),
    path("random/", views.random_page, name="random_page"),
    path("edit/<str:heading>/" ,views.edit, name="edit")


]
