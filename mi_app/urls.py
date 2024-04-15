from django.urls import path
from .views import hello_world

urlpatterns = [
    # Define la ruta para la vista hello_world
    path('', hello_world)
]
