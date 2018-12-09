from django.contrib import admin
from . import models
# Register your models here.

# @admin.register(models.UserProfile)
# class ProfileAdmin(admin.ModelAdmin):

admin.site.register(models.UserProfile)
admin.site.register(models.Events)
