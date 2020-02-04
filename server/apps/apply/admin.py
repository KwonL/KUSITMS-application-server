from django.contrib.admin.decorators import register
from django.contrib.admin import ModelAdmin
from apps.apply.models import ApplyForm


@register(ApplyForm)
class ApplyFormAdmin(ModelAdmin):
    pass
