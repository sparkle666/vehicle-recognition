from django.urls import path

from .views import (HomePageView, superuser_signup, vehicle_image_list)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('vehicle-list/', vehicle_image_list, name='vehicle_image_list'),

    # Accounts
    path('superuser/signup/', superuser_signup, name='superuser_signup'),

]
