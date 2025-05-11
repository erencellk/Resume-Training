from django.contrib import admin
from core.models import *


# Register your models here.

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_date', 'updated_date', 'parameter']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

    class Meta:
        model = GeneralSetting


@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'file']
    list_editable = ['description', 'file']

    class Meta:
        model = ImageSetting


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'percentage', 'updated_date', 'created_date']
    search_fields = ['name']
    list_editable = ['order', 'name', 'percentage']

    class Meta:
        model = Skill


@admin.register(Capabilities)
class CapabilitiesAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'link', 'updated_date', 'created_date']
    search_fields = ['name']
    list_editable = ['order', 'name', 'link']

    class Meta:
        model = Capabilities

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'email', 'phone', 'message']
    search_fields = ['name']


    class Meta:
        model = Message
