
from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=200, null = True, blank = False)
    def __str__(self):
        return self.email


class VehicleImage(models.Model):
    image = models.ImageField(upload_to='vehicle_images/')
    plate_number = models.CharField(max_length=20, blank = True, null = True)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(CustomUser, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return f"Vehicle-{self.id} - {self.created_at}"

