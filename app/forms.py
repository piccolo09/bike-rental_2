from django import forms
from .models import MyUser,BikeAd
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.core.validators import RegexValidator

class authentication_form(AuthenticationForm):
    use_required_attribute = False

class createuser_form(UserCreationForm):
    use_required_attribute = False
    mobile = forms.CharField(min_length=10,max_length=10,required=True,label="Number")
    email = forms.EmailField(required=True,label = "Email")
    
    class Meta:
        model = MyUser
        fields = ("username","email","mobile")

class UpdateUserForm(forms.ModelForm):
    use_required_attribute = False
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))  
      
    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',}))
    
    last_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    mobile = forms.CharField(min_length=10,max_length=10,
                               required=True,
                               widget=forms.TextInput(attrs={'cols': 1,'class': 'form-control','type':'number',}))

    address = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control','rows':3}))


    class Meta:
        model = MyUser
        fields = ['username', 'first_name','last_name','email','mobile','address']

class createuserad_form(forms.ModelForm):
    use_required_attribute = False
    class Meta:
        model = BikeAd
        fields = '__all__'