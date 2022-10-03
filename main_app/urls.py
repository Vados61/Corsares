from django.urls import path

from main_app.views import index, new_character

urlpatterns = [
    path('', index),
    path('new/', new_character)
]