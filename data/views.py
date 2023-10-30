from django.shortcuts import render

def home(request):
    welcome_message = "Welcome to our awesome Django app!"
    return render(request, 'myapp/home.html', {'welcome_message': welcome_message})
