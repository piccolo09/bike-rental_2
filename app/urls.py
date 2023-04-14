from django.urls import path
from .views import HomeView,AboutusView,TopGView,BikePageView,MyProfileView
urlpatterns = [
    path('',HomeView.as_view(),name="Home"),
    path('aboutus/',AboutusView.as_view(),name="aboutus"),
    path('topg/',TopGView.as_view(),name="TopG"),
    path('bikeview/',BikePageView.as_view(),name="bikeview"),
    path('myprofile/',MyProfileView.as_view(),name="myprofile"),

]
