from django.shortcuts import render

def index(request):
    return render(request, 'templates\\index.html')

def contact(request):
    return render(request, 'templates\\contact.html')
