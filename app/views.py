from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import MyUser

# Create your views here.

class HomeView(View):

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
            return HttpResponseRedirect("/")
        else:
            return render(request, "app/home.html", {"isLogined": request.user.is_authenticated})

    # Get Method
    def get(self, request):
        print('help')
        request.session.modified = True
        request.session['Hello'] = 'Hello'
        print(request.session['Hello'])
        return render(request, "app/home.html", locals())

    # Post Method
    def post(self, request, **kwargs):
        request.session.modified = True
        request.session["Hello"] = "Hello"
        # if 'Logoutbutton' in request.POST:
        #     logout(request)
        #     return HttpResponseRedirect("/")
        # elif "Signinbutton" in request.POST:
        #     username = request.POST.get("SigninInputUsername")
        #     password = request.POST.get("SigninInputPassword")
        #     # return self.authme_setme(request, username, password)
        #     user_obj = authenticate(request, username=username, password=password)
        #     if user_obj is not None:
        #         login(request, user_obj)
        #         user_Queryset = MyUser.objects.filter(username=username)
        #         for user_data in user_Queryset.values():
        #             request.session['id'] = user_data['id']
        #             request.session['username'] = user_data['username']
        #             request.session['first_name'] = user_data['first_name']
        #             request.session['last_name'] = user_data['last_name']
        #             request.session['email'] = user_data['email']
        #             request.session['mobile'] = user_data['mobile']
        #             request.session['address'] = user_data['address']
        #         return HttpResponseRedirect("/")
        #     else:
        #         return render(request, "app/home.html", {"isLogined": request.user.is_authenticated})
        # elif "Signupbutton" in request.POST:
        #     username = request.POST.get("SignupInputUsername")
        #     email = request.POST.get("SignupInputEmail")
        #     password = request.POST.get("SignupInputPassword")
        #     confirm_password = request.POST.get("SignupInputPasswordConfirm")
        #     if password == confirm_password:
        #         my_user = MyUser.objects.create_user(username=username, email=email, password=password)
        #         my_user.save()
        #         self.authme_setme(request, username, password)
        #         return HttpResponse("hoagay")
        #     else:
        #         return HttpResponse("galat pass word hai bsdk")



class AboutusView(View):
    def get(self, request):
        return render(request, "app/aboutus.html", locals())


class TopGView(View):
    def get(self, request):
        return render(request, "app/topg.html", locals())


class BikePageView(View):
    def get(self, request):
        return render(request, "app/bikeview.html", locals())


class MyProfileView(View):
    def get(self, request):
        return render(request, "app/myprofile.html", locals())
