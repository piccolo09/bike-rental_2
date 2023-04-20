from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import HomeView,AboutusView,TopGView,BikePageView,MyProfileView
urlpatterns = [

    #Home View
    path('',HomeView.as_view(),name="home"),
    
    #About Us
    path('aboutus/',AboutusView.as_view(),name="aboutus"),
    
    #View Bike Individually
    path('bikeview/',BikePageView.as_view(),name="bikeview"),

    #Individual User View
    path('myprofile/',MyProfileView.as_view(),name="myprofile"),

    #Easter Egg
    path('topg/',TopGView.as_view(),name="TopG"),

]


