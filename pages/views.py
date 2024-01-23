from django.views.generic import TemplateView
from accounts.models import CustomUser
from django.shortcuts import redirect, render, get_object_or_404
from .forms import SuperuserCreationForm, VehicleImageEditForm
from django.http import HttpResponse
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages
from accounts.models import VehicleImage
from .utils import ocr_image


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


def projects_list(request):

    context = {'projects': "projects"}

    return render(request, 'pages/project_list.html', context)


def vehicle_image_list(request):
    vehicle_images = VehicleImage.objects.all()
    return render(request, 'pages/vehicle_image_list.html', {'vehicle_images': vehicle_images})


def send_sms(request, id):
    vehicle_image = VehicleImage.objects.get(id=id)
    users = CustomUser.objects.all()

    return render(request, 'pages/send_sms.html', {'vehicle_image': vehicle_image, "users": users})


def generate_ocr(request, id):
    vehicle_image = VehicleImage.objects.get(id=id)
    print("path", vehicle_image.image.path)
    print("Generating...")
    number = ocr_image(vehicle_image.image.path)
    if number:
        vehicle_image.plate_number = number
        vehicle_image.save()
        print("Generated success")
    return redirect("vehicle_image_list")
    # return render(request, 'pages/vehicle_image_list.html', {})


def edit_plate_number(request, vehicle_image_id):
    vehicle_image = get_object_or_404(VehicleImage, id=vehicle_image_id)

    if request.method == 'POST':
        form = VehicleImageEditForm(request.POST, instance=vehicle_image)
        if form.is_valid():
            form.save()
            return redirect('vehicle_image_list')
    else:
        form = VehicleImageEditForm(instance=vehicle_image)

    return render(request, 'pages/edit_plate_number.html', {'form': form, 'vehicle_image': vehicle_image})


def sms_success(request):
    # vehicle_images = VehicleImage.objects.all()
    return render(request, 'pages/sms_success.html', {})


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
