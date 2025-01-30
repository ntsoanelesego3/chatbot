from django.contrib import admin
from .models import user_login
from .models import user_register

# Register your models here.
admin.site.register(user_login)
admin.site.register(user_register)
