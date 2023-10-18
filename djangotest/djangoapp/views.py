from django.shortcuts import render

# Create your views here.

def home(request):
    context = {"name": "Junior"}
    return render(request, "djangoapp/home.html", context)
