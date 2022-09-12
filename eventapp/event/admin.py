from django.contrib import admin
from .models import *
from django.utils.html import format_html

class EventAdmin(admin.ModelAdmin):
    list_display= ('name','description','icon')


class SpeakerAdmin(admin.ModelAdmin):
    def photo_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.photo.url))
    list_display= ('name','photo')

class SessionAdmin(admin.ModelAdmin):
    fields= ['speakers']
    list_display=('name','nombre_speakers','date','hour')


admin.site.register(Event,EventAdmin)
admin.site.register(Speaker,SpeakerAdmin)
admin.site.register(Session,SessionAdmin)
# Register your models here.
