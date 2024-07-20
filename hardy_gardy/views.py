from django.shortcuts import render
from .forms import UserAuthorizationForm, UserRegistrationForm
from .models import Form


def sign_in(request):
    if request.method == 'POST':
        form = UserAuthorizationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            Form.objects.create(username=username, password=password)
    return render(request, "sign_in.html")


def sign_up(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # user_id = form.cleaned_data['user_id']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            Form.objects.create(username=username, password=password)
    return render(request, "sign_up.html")

def registrastion(request):
    print("----->>>>>  registrasion")
    return render(request, "registrastion.html")


def main_menu(request):
    return render(request, "main_menu.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
