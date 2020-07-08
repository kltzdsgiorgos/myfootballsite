from django.contrib import admin
from .models import EnglandFixtures, JapanFixtures, GermanFixtures

# Register your models here.

admin.site.register(EnglandFixtures)
admin.site.register(GermanFixtures)
admin.site.register(JapanFixtures)
