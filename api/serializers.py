# serializers.py
from rest_framework import serializers
from accounts.models import VehicleImage


class VehicleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleImage
        fields = ('id', 'image', 'plate_number',)
