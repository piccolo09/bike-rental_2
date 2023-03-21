from django.urls import path
from .views import HomeView,AboutusView,TopGView
urlpatterns = [
    path('',HomeView.as_view(),name="Home"),
    path('aboutus/',AboutusView.as_view(),name="aboutus"),
    path('topg/',TopGView.as_view(),name="TopG"),
]
