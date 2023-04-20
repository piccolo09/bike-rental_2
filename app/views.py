from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import MyUser
from .forms import authentication_form,createuser_form



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
                request.session['username'] = user_data['username']
                request.session['first_name'] = user_data['first_name']
                request.session['last_name'] = user_data['last_name']
                request.session['email'] = user_data['email']
                request.session['mobile'] = user_data['mobile']
                request.session['address'] = user_data['address']

    # Get Method
    def get(self,request):
        # form = authentication_form()
        # form2 = createuser_form()
        return render(request,"app/home.html",{'form':form,'form2':form2})

    # Post Method
    def post(self, request, **kwargs):
        form = authentication_form()
        form2 = createuser_form()
        if 'Logoutbutton' in request.POST:
            logout(request)
            return HttpResponseRedirect("/")
        elif "Signinbutton" in request.POST:
            form = authentication_form(request=request, data=request.POST)
            if form.is_valid():
                self.authme_setme(request, request.POST.get('username'), request.POST.get('password'))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
                # return render(request,"app/home.html",{'form':form,'form2':form2,'form_error':0})
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
    def get(self, request):
        return render(request, "app/bikeview.html", {'form':form,'form2':form2})

# Individual User Profile
class MyProfileView(View):
    def get(self, request):
        print(request.user)
        # if :
        return render(request, "app/myprofile.html", {'form':form,'form2':form2})
        # else:
        #     return render(request,"app/home.html")
            
