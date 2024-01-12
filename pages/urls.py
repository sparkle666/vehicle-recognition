from django.urls import path

from .views import (HomePageView, superuser_signup, vehicle_image_list, send_sms, sms_success)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('vehicle-list/', vehicle_image_list, name='vehicle_image_list'),
    path('send-sms/', send_sms, name='send_sms'),
    path('sms-success/', sms_success, name='sms_success'),

    # Accounts
    path('superuser/signup/', superuser_signup, name='superuser_signup'),

]
