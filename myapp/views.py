from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
  # return HttpResponse("Hello, World")
  return render(request, "home.html") # Renders 'home.html' in the templates directory

def todos(request):
  items = TodoItem.objects.all()
  return render(request, "todos.html", {"todos": items})
