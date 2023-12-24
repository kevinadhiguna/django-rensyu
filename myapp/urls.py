from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), # Calls 'home()' in views.py
    path("todos/", views.todos, name="Todos")
]

