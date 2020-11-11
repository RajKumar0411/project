from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    #used for creating label
    username = forms.CharField(max_length=100,label="Username")
    password = forms.CharField(max_length=100,label="Password",widget=forms.PasswordInput)


    def clean(self):
        # used for cleaning data after login or incorrect information
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        
        if username and password:
            user = authenticate(username=username,password=password)
            
            if not user:
                raise forms.ValidationError("Username or Password not correct!")
            return super(LoginForm, self).clean()





class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()

        return user         