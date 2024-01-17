from django.shortcuts import render
from accounts.models import VehicleImage

from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import VehicleImageSerializer


class ImageUploadView(generics.CreateAPIView):
    queryset = VehicleImage.objects.all()
    serializer_class = VehicleImageSerializer
    parser_classes = (MultiPartParser, FormParser)
