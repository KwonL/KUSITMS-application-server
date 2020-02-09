from django.contrib.admin.decorators import register
from django.contrib.admin import ModelAdmin
from apps.account.models import User


@register(User)
class UserAdmin(ModelAdmin):
    search_fields = ['username', 'email']
