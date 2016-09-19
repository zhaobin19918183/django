from django.contrib import admin
from .models import UserGroup,UserInfo,UserProfile

admin.site.register(UserGroup)
admin.site.register(UserInfo)
admin.site.register(UserProfile)