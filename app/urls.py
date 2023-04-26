from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *
urlpatterns = [

    #Home View
    path('',HomeView.as_view(),name="home"),
    
    #About Us
    path('aboutus/',AboutusView.as_view(),name="aboutus"),
    
    #View Bike Individually
    path('bikeview/<int:id>',BikePageView.as_view(),name="bikeview"),

    #All Bike VIew 
    path('bikelisting/<slug:biketype>',BikelistingPageView.as_view(),name="allbikeview"),

    #Individual User View
    path('myprofile/',MyProfileView.as_view(),name="myprofile"),

    #Individual User Ads
    path('managemyads/',MyAdsView.as_view(),name="managemyads"),

    path('myad/<int:id>',UpdateAds.as_view(),name="updatead"),

    #WishList
    path('wishlist/add_to_whishlist/<int:id>',UserWishActionView.as_view(),name="user_wishlist"),

    path('wishlist/',UserWishView.as_view(),name="see_wishlist"),


    #Easter Egg
    path('topg/',TopGView.as_view(),name="TopG"),

]   


