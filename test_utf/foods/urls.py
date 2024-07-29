from django.urls import path

from .views import get_food



urlpatterns = [
    path('', get_food, name='get_food'),

]
