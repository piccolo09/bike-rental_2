from django.db import models


# Create your models here.
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
        ("YES","YES"),
        ("NO","NO"),
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
    bike_image = models.ImageField(upload_to ='uploads/')
    # bike_ownerID = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.bike_name

# class AppUser(models.Model):
#     user_name = models.C