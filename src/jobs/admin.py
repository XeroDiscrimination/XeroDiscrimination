from django.contrib import admin

from .models import Job, Application


class JobAdmin(admin.ModelAdmin):
    "" ""

admin.site.register(Job, JobAdmin)
admin.site.register(Application)
