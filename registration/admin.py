from django.contrib import admin
from .models import CustomUser, RegisterUser
admin.site.register(CustomUser)
admin.site.register(RegisterUser)
