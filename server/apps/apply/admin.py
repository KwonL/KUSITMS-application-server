from django.contrib.admin import ModelAdmin
from django.contrib.admin.decorators import register

from apps.apply.models import ApplyForm, SNSImage, SiteConfig, ApplyConfig


@register(SiteConfig)
class SiteConfigAdmin(ModelAdmin):
    pass


@register(ApplyConfig)
class ApplyConfigAdmin(ModelAdmin):
    pass


@register(ApplyForm)
class ApplyFormAdmin(ModelAdmin):
    autocomplete_fields = ['user']


@register(SNSImage)
class SNSImageAdmin(ModelAdmin):
    pass
