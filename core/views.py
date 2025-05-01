from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, 'templates/index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print(f"İletişim Formu: {name} - {email} - {subject} - {message}")
        messages.success(request, 'Your message has been sent!.')
        return redirect('/#contact')
    return redirect('/#contact')
