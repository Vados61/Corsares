from django.shortcuts import render


def index(request):
    return render(request, 'base.html')


def new_character(request):
    return render(request, 'new_character.html')
