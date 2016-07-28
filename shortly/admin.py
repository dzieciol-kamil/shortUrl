from django.contrib import admin

# Register your models here.

from .models import Urls
admin.site.register(Urls)

from .models import UserProfile
admin.site.register(UserProfile)