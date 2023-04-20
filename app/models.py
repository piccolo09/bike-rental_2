from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=50,blank=True)
    address = models.TextField(blank=True)

class BikeAd(models.Model):
    BIKETYPE_CHOICE = (
        ("Touring", "Touring"),
        ("Sports", "Sports"),
        ("Mopads", "Mopads"),
        ("Naked", "Naked"),
    )

    BIKEBRAND_CHOICE = (
        ("KTM", "KTM"),
        ("BAJAJ", "BAJAJ"),
        ("BMW", "BMW"),
        ("TVS", "TVS"),
        ("HERO", "HERO"),
        ("HONDA", "HONDA"),
    )

    YESNO_CHOICE = (
        ("YES", "YES"),
        ("NO", "NO"),
    )

    bike_name = models.CharField(max_length=50)
    bike_type = models.CharField(max_length=50, choices=BIKETYPE_CHOICE, default="")
    bike_discription = models.TextField()
    bike_rent_price = models.FloatField()
    bike_brand = models.CharField(max_length=50, choices=BIKEBRAND_CHOICE, default="")
    bike_engine_size = models.IntegerField()
    bike_mileage = models.FloatField()
    bike_fueltank_size = models.IntegerField()
    bike_weight = models.IntegerField()
    bike_has_abs = models.CharField(max_length=50, choices=YESNO_CHOICE, default="NO")
    bike_topspeed = models.IntegerField()
    bike_image = models.ImageField(upload_to='uploads/')
    # bikead_ownerID = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    is_active = models.BooleanField(default=True, verbose_name='active')



    def __str__(self):
        return self.bike_name
