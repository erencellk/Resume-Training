from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import GeneralSetting, ImageSetting


def index(request):

    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameter
    about_me_capabilities = GeneralSetting.objects.get(name='about_me_capabilities').parameter

    home_favicon= ImageSetting.objects.get(name='home_favicon').file
    personal_picture = ImageSetting.objects.get(name='personal_picture').file


    context = {
        'site_title': site_title,
        'site_keywords':site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_description': home_banner_description,
        'about_me_capabilities': about_me_capabilities,
        'home_favicon': home_favicon,
        'personal_picture': personal_picture,
    }
    return render(request, 'templates/index.html' , context=context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print(f"Communication Form: {name} - {email} - {subject} - {message}")
        messages.success(request, 'Your message has been sent!')
        return redirect('/#contact')
    return redirect('/#contact')
