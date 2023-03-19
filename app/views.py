from django.shortcuts import render
from django.views import View

# Create your views here.

class HomeView(View):
    def get(self,request):
        return render(request,"app/home.html",locals())
    
class AboutusView(View):
    def get(self,request):
        return render(request,"app/aboutus.html",locals())
