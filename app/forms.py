from django import forms
from .models import MyUser
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class login_MyUser(forms.Form):
    use_required_attribute = False
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,widget=forms.PasswordInput)

    def clean_username(self):
        value_username = self.cleaned_data['username']
        if len(value_username) < 4:
            raise forms.ValidationError("Enter more then or equal 4 charaters")
        elif not(MyUser.objects.filter(username=value_username).exists()):
            raise forms.ValidationError("Invaild Username")
    
    # def clean_password(self):
        # value_username = self.cleaned_data['username']
        # value_password = self.cleaned_data['password']
        # value_oldpassword=MyUser.objects.filter(username=value_username).values('password')

        # if value_oldpassword != value_password

        
class authentication_form(AuthenticationForm):
    use_required_attribute = False

class createuser_form(UserCreationForm):
    use_required_attribute = False
    email = forms.EmailField(required=True,label = "Email")
    
    class Meta:
        model = MyUser
        fields = ("username", "email",)
