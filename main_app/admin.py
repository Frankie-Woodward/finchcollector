from django.contrib import admin

from .models import Ev, Charging

# Register your models here.

admin.site.register(Ev)
admin.site.register(Charging)