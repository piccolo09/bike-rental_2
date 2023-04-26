from django.shortcuts import render, HttpResponseRedirect, redirect,get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import MyUser,BikeAd
from .forms import authentication_form,createuser_form,UpdateUserForm,createuserad_form



# Create your views here.

form = authentication_form()
form2 = createuser_form()

# Home View
class HomeView(View):
    # form = authentication_form()
    # singup_form = createuser_form()

    # Authenticat & Set Session Method
    def authme_setme(self,request, username, password):
        user_obj = authenticate(request, username=username, password=password)
        if user_obj is not None:
            login(request, user_obj)
            user_Queryset = MyUser.objects.filter(username=username)
            for user_data in user_Queryset.values():
                request.session['id'] = user_data['id']

    # Get Method
    def get(self,request):
        form = authentication_form()
        form2 = createuser_form()
        availableads = BikeAd.objects.filter(is_active=True).order_by('-id')[0:10]
        return render(request,"app/home.html",locals())

    # Post Method
    def post(self, request, **kwargs):
        form = authentication_form()
        form2 = createuser_form()
        if 'Logoutbutton' in request.POST:
            logout(request)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        elif "Signinbutton" in request.POST:
            form = authentication_form(request=request, data=request.POST)
            if form.is_valid():
                self.authme_setme(request, request.POST.get('username'), request.POST.get('password'))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
            else:
                return render(request,"app/home.html",{'form':form,'form2':form2,'form_error':1})
        elif "Signupbutton" in request.POST:
            form2 = createuser_form(request.POST)
            if form2.is_valid():
                form2.save()  
                return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
            else:
                return render(request,"app/home.html",{'form':form,'form2':form2,'form2_error':1})

#AboutUs View
class AboutusView(View):
    def get(self, request):
        return render(request, "app/aboutus.html", {'form':form,'form2':form2})

#EasterEgg
class TopGView(View):
    def get(self, request):
        return render(request, "app/topg.html",{'form':form,'form2':form2})

# Individual Bike View
class BikePageView(View):
    def get(self, request,id): 
        form = authentication_form()
        form2 = createuser_form()
        availablead = BikeAd.objects.get(id=id,is_active=True)
        if(availablead):
            ownerID = availablead.bikead_ownerID
            print(ownerID)
            bikeowner = MyUser.objects.get(id=ownerID.id)
            return render(request, "app/bikeview.html",locals())
        else:
            return render(request, "app/bikeview.html",locals())
    
# All Bike Ads
class BikelistingPageView(View):
    def get(self, request,biketype):
        form = authentication_form()
        form2 = createuser_form()
        availableads = BikeAd.objects.filter(bike_type=biketype,is_active=True)
        return render(request, "app/bikelisting.html", locals())

# Individual User Profile
class MyProfileView(View):
    def get(self, request):
        form = authentication_form()
        form2 = createuser_form()
        if request.user.is_authenticated:
            user_form = UpdateUserForm(instance=request.user)
            user_info = MyUser.objects.get(id=request.session['id'])
        return render(request, "app/myprofile.html", locals())
    
    def post(self, request):
        user_form = UpdateUserForm(request.POST,instance=request.user)
        if user_form.is_valid(): 
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='myprofile')
        else:
            user_info = MyUser.objects.get(id=request.session['id'])
            return render(request, "app/myprofile.html", locals())


# Individual User Ads
class MyAdsView(View):
    def get(self, request):
        form = authentication_form()
        form2 = createuser_form()
        myadform = createuserad_form()
        if request.user.is_authenticated:
            user_id = request.session['id']
            users_bikes = BikeAd.objects.filter(bikead_ownerID=request.session['id']).order_by('-id')
        return render(request, "app/managemyads.html", locals())

    def post(self, request):
        myadform = createuserad_form(request.POST,files=request.FILES)
        users_bikes = BikeAd.objects.filter(bikead_ownerID=request.session['id']).order_by('-id')
        if myadform.is_valid(): 
            myadform.save()
            messages.success(request, 'Your Ad is Added successfully')
            return redirect(to='managemyads')
        else:
            user_info = MyUser.objects.get(id=request.session['id'])
            return render(request, "app/managemyads.html", locals())

# Individual Ads update
class UpdateAds(View):
    def get(self, request,id):
        form = authentication_form()
        form2 = createuser_form()
        post = get_object_or_404(BikeAd, id=id)
        myadform = createuserad_form(request.POST or None, request.FILES or None, instance=post)
        if request.user.is_authenticated:
            user_id = request.session['id']
            users_bikes = BikeAd.objects.filter(bikead_ownerID=request.session['id']).order_by('-id')
        return render(request, "app/updatead.html", locals())
    
    def post(self, request,id):
        post = get_object_or_404(BikeAd, id=id)
        myadform = createuserad_form(request.POST or None, request.FILES or None, instance=post)
        if myadform.is_valid(): 
            myadform.save()
            messages.success(request, 'Updated successfully')
            return redirect(to='managemyads')
        else:
            return render(request, "app/updatead.html", locals())
        

# User Wish List
class UserWishActionView(View):
    def get(self, request,id):
        form = authentication_form()
        form2 = createuser_form()
        product = get_object_or_404(BikeAd, id=id)
        if request.user.is_authenticated:
            if product.user_wishlist.filter(id=request.session['id']).exists():
                product.user_wishlist.remove(request.user)
                messages.error(request, 'Removed from wishlist')
            else:
                product.user_wishlist.add(request.user)
                messages.success(request, 'Added to wishlist')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

class UserWishView(View):
    def get(self, request):
        form = authentication_form()
        form2 = createuser_form()
        if request.user.is_authenticated:
            wishlist_bikes = BikeAd.objects.filter(user_wishlist=request.user).order_by('-id')
        return render(request, "app/wishlist.html", locals())
