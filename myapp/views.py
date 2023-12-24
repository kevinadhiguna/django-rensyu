from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
  # return HttpResponse("Hello, World")
  return render(request, "home.html") # Renders 'home.html' in the templates directory
