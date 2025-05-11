from django.contrib.messages.api import success
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import GeneralSetting, ImageSetting, Skill, Capabilities, Message


def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    home_banner_name = GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_description = GeneralSetting.objects.get(name='home_banner_description').parameter
    about_me_capabilities = GeneralSetting.objects.get(name='about_me_capabilities').parameter

    home_favicon = ImageSetting.objects.get(name='home_favicon').file
    personal_picture = ImageSetting.objects.get(name='personal_picture').file

    skills = Skill.objects.all().order_by('order')
    capabilities = Capabilities.objects.all().order_by('order')

    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_description': home_banner_description,
        'about_me_capabilities': about_me_capabilities,
        'home_favicon': home_favicon,
        'personal_picture': personal_picture,
        'skills': skills,
        'capabilities': capabilities,
    }
    return render(request, 'templates/index.html', context=context)


def contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message_text = request.POST.get("message")

        Message.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message_text
        )

        messages.success(request, 'Message has been sent.')
        return render(request , 'templates/index.html')
    else:
        success = False
        message = 'Request method is not valid.'

    context = {
        'success': success,
        'message': message,
    }

    return JsonResponse(context)


def contact(request):
    return render(request, 'templates/index.html')
