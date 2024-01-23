from django import forms
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from accounts.models import VehicleImage


class SuperuserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)



class VehicleImageEditForm(forms.ModelForm):
    class Meta:
        model = VehicleImage
        fields = ['plate_number', "approved"]
