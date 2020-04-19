from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('email',)


# Register your models here.
admin.site.register(User, UserAdmin)
