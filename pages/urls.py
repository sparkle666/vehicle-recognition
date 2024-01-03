from django.urls import path

from .views import (HomePageView, superuser_signup,)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),

    # Accounts
    path('superuser/signup/', superuser_signup, name='superuser_signup'),

]
