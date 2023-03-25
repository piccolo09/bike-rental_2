from django.shortcuts import render
from django.views import View

# Create your views here.

class HomeView(View):
    def get(self,request):
        return render(request,"app/home.html",locals())
    
class AboutusView(View):
    def get(self,request):
        return render(request,"app/aboutus.html",locals())

class TopGView(View):
    def get(self,request):
        return render(request,"app/topg.html",locals())

class BikePageView(View):
    def get(self,request):
        return render(request,"app/bikeviewpage.html",locals())
