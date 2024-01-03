from django.views.generic import TemplateView
from accounts.models import CustomUser
from django.shortcuts import redirect, render, get_object_or_404
from .forms import  SuperuserCreationForm
from django.http import HttpResponse
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"



def projects_list(request):
    
    context = {'projects': "projects"}

    return render(request, 'pages/project_list.html', context)


def superuser_signup(request):
    if request.method == 'POST':
        form = SuperuserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = True
            user.is_staff = True
            user.save()

            # Log in the superuser
            user = auth.authenticate(
                username=user.username, password=request.POST['password1'])
            if user is not None:
                auth.login(request, user)

            # Redirect to the admin dashboard.
            return redirect(reverse('admin:index'))
    else:
        form = SuperuserCreationForm()
    return render(request, 'account/superuser_signup.html', {'form': form})
