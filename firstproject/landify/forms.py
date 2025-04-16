from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserResponse
from .models import ContactSubmission

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserResponseForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = [
            'location_text',
            'state',
            'district',
            'pincode',
            'rate',
            'way',
            'picture',
            'phone_number',
            'area'
        ]
        widgets = {
            'way': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')])
        }
        labels = {
            'rate': 'Rate (in sq ft)',
            'area': 'Area (in sq ft)',
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'phone', 'subject', 'message']