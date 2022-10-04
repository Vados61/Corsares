from django.shortcuts import render

from map.map import map


def index(request):
    context = {
        'map': map.values()
    }
    return render(request, 'base.html', context)


def new_character(request):
    return render(request, 'new_character.html')
