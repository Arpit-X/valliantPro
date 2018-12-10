from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user","phone","college","joinedOn","isCoordinator","isFaculty")


admin.site.register(models.Participations)
@admin.register(models.Location)
class LocationInline(admin.ModelAdmin):
    list_display = ("name", "longitude","latitude")

@admin.register(models.Events)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name","facultyCoordinator","studentCoordinator","totalPraticipants","isSpot")
