from django.contrib.admin import ModelAdmin, StackedInline
from django.contrib.admin.decorators import register

from apps.apply.models import (
    ApplyForm,
    SNSImage,
    SiteConfig,
    ApplyConfig,
    MainSlideImage,
    MailList,
)


class SlideInline(StackedInline):
    model = MainSlideImage
    extra = 1


@register(SiteConfig)
class SiteConfigAdmin(ModelAdmin):
    inlines = [SlideInline]
    list_display = ["generation", "president", "vice_president"]


@register(ApplyConfig)
class ApplyConfigAdmin(ModelAdmin):
    list_display = ["name", "is_active"]


@register(ApplyForm)
class ApplyFormAdmin(ModelAdmin):
    autocomplete_fields = ["user"]
    list_display = ["name", "university", "birth"]


@register(SNSImage)
class SNSImageAdmin(ModelAdmin):
    pass


@register(MailList)
class MailListAdmin(ModelAdmin):
    list_display = ["name", "email"]
