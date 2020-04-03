from django import forms

# import GeeksModel from models.py
from .models import user
from .models import post

# create a ModelForm
class UserForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = user
        fields = "__all__"

class UserPost(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = post
        fields = "__all__"

