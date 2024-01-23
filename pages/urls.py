from django.urls import path

from .views import (HomePageView, superuser_signup,
                    vehicle_image_list, send_sms, generate_ocr, edit_plate_number, sms_success)


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('vehicle-list/', vehicle_image_list, name='vehicle_image_list'),
    path('send-sms/<int:id>', send_sms, name='send_sms'),
    path('sms-success/', sms_success, name='sms_success'),
    path('generate-ocr/<int:id>', generate_ocr, name='generate_ocr'),
    path('edit-plate-number/<int:vehicle_image_id>/',
         edit_plate_number, name='edit_plate_number'),

    # Accounts
    path('superuser/signup/', superuser_signup, name='superuser_signup'),

]
