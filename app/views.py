from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login,logout

# Create your views here.

class HomeView(View):
    def get(self,request):
        return render(request,"app/home.html",locals())
    
    def post(self, request, **kwargs):
        if 'Logoutbutton' in request.POST:
            logout(request)
            return HttpResponseRedirect("/")
        elif "Signinbutton" in request.POST:
            username = request.POST.get("SigninInputUsername")
            password = request.POST.get("SigninInputPassword")
            user_obj = authenticate(request,username=username,password=password)
            if user_obj is not None:
                login(request,user_obj)
                return HttpResponseRedirect("/")
            else:
                return render(request,"app/home.html",{"isLogined":request.user.is_authenticated})
        elif "Signupbutton" in request.POST:
            print("SIngup")
        

class AboutusView(View):
    def get(self,request):
        return render(request,"app/aboutus.html",locals())

class TopGView(View):
    def get(self,request):
        return render(request,"app/topg.html",locals())

class BikePageView(View):
    def get(self,request):
        return render(request,"app/bikeview.html",locals())

class MyProfileView(View):
    def get(self,request):
        return render(request,"app/myprofile.html",locals())
