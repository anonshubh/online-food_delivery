from allauth.account.forms import SignupForm , LoginForm
from django import forms
from allauth.account.adapter import DefaultAccountAdapter 
from django.forms import ValidationError

from .models import UserInfo


class CustomLoginForm(LoginForm):
     def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs = {'placeholder': 'Username or Email', 'autofocus': 'autofocus'}


class CustomSignupForm(SignupForm):
    """
    Custom SignUp Form and Also Created New user_info Object
    """

    first_name = forms.CharField(max_length=30, label='First Name') 
    last_name = forms.CharField(max_length=30, label='Last Name')
    signup_as_restaurant = forms.BooleanField()

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)

        user.first_name = self.cleaned_data['first_name'] 
        user.last_name = self.cleaned_data['last_name']

        signup_as_restaurant = self.cleaned_data['signup_as_restaurant']

        user.save()

        # age = self.cleaned_data['age']
        # gender = self.cleaned_data['gender']
        # phone = str(self.cleaned_data['phone'])
        # department_year = self.cleaned_data['department_year']

        user_info , created = UserInfo.objects.get_or_create(
            user=user,
            is_restaurant = signup_as_restaurant
        )

        return user
