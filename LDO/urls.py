from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('compose/<int:id>', views.composeLDO, name="compose"),
]