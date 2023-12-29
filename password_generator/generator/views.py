from django.shortcuts import render
import random
import string


def home(request):
    return render(request, "generator/home.html")


def password(request):
    the_password = ""
    characters = list(string.ascii_lowercase)
    if request.GET.get("uppercase"):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get("special"):
        characters.extend(list(string.punctuation))
    if request.GET.get("numbers"):
        characters.extend(list(string.digits))
    length = int(request.GET.get("length", 12))
    for _ in range(length):
        the_password += random.choice(characters)

    return render(request, "generator/password.html", {"password": the_password})


def about(request):
    return render(request, "generator/about.html")
