from django.contrib import admin

# Register your models here.
from app.models import Activation


class ActivationAdmin(admin.ModelAdmin):
    fields = ['user', 'code', 'email']
    list_display = ('user', 'code', 'email')
    search_fields = ('user', 'code', 'email')

    admin.site.register(Activation)