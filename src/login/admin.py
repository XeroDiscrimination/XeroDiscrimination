from django.contrib import admin

# Register your models here.

from . import models

class UserAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    search_fields = ('name', 'email')
    list_display = ('name','pronoun','email')

admin.site.register(models.User, UserAdmin)