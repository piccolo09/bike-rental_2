from django.contrib import admin
from django.urls import path
from .views import HomeView,AboutusView
urlpatterns = [
    path('/',HomeView.as_view(),name="Home"),
    path('aboutus/',AboutusView.as_view(),name="AboutUs"),
]
