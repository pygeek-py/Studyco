from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import movieimg, box

class registerform(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    
    class Meta():
        model = User
        fields = ["first_name", "username", "email", "password1", "password2"]


class imgform(forms.ModelForm):

	class Meta():
		model = movieimg
		fields = '__all__'
		exclude = ["user"]
		widgets = {
            'bio': forms.TextInput(attrs={'id': 'ink'}),
        }

class boxform(forms.ModelForm):

    class Meta():
        model = box
        fields = ["based"]
        exclude = []