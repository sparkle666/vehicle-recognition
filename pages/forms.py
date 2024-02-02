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


class SMSSendForm(forms.Form):

    users = CustomUser.objects.all()
    user_choices = [(user.username, user.username) for user in users]

    user = forms.ChoiceField(label='Select User', choices=user_choices,
                             widget=forms.Select(attrs={'class': 'form-select'}))

    # user = forms.ModelChoiceField(label='Select User', queryset=CustomUser.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    phoneNumber = forms.CharField(
        label='Phone Number', widget=forms.TextInput(attrs={'class': 'form-control'}), initial='07010996153')
    message = forms.CharField(label='Message', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3}), initial="Your license number is: ")
