from django.contrib import admin
from . import models
from .models import Profile





#------------------------------------------------------------------------------
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'user_name','phone','address')
    search_fields = ['user_name', 'phone', 'address']

admin.site.register(models.Profile, ProfileAdmin)
