from django.shortcuts import render

def home(request):
    welcome_message = "Welcome to our website! \n We are Here to help you with your all designs "
    return render(request, 'myapp/home.html', {'welcome_message': welcome_message})
