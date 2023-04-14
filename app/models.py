from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager,UserManager,User,AbstractUser
# class CustomUserManager(BaseUserManager):
    
#     def _create_user(self, email, password, **extra_feilds):
#         if not email:
#             raise ValueError("Email must be provider")
#         if not password:
#             raise ValueError("Password must be provider")

#         user = self.model(
#             email=self.normalize_email(email),
#             **extra_feilds
#         )
#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_user(self, email, password, **extra_fields):
#         print("Create Called")
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
        
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")
#         return self._create_user(email, password, **extra_fields)

# # Create your models here.


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True, max_length=245)
#     username = models.CharField(max_length=245,null=True)
#     first_name = models.CharField(max_length=245,blank=True)
#     last_name = models.CharField(max_length=245,blank=True)
#     mobile = models.CharField(max_length=50,blank=True)
#     address = models.TextField()

#     is_superuser = models.BooleanField(default=False, verbose_name='superuser',blank=True)
#     is_staff = models.BooleanField(default=False, verbose_name='staff',blank=True)
#     is_active = models.BooleanField(default=True, verbose_name='active',blank=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name'] # Email & Password are required by default.

#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'

#     def __str__(self):
#         return self.email

class MyUser(AbstractUser):
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
