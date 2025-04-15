from django.contrib import admin

# Register your models here.
from .models import emplayee,job,sign,user_login
admin.site.register(emplayee),
admin.site.register(job),
admin.site.register(sign),
admin.site.register(user_login)