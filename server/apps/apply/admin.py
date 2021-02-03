from django.contrib.admin import ModelAdmin, StackedInline
from django.contrib.admin.decorators import register

from apps.apply.models import (
    ApplyForm,
    SNSImage,
    SiteConfig,
    ApplyConfig,
    MainSlideImage,
)


class SlideInline(StackedInline):
    model = MainSlideImage
    extra = 1


@register(SiteConfig)
class SiteConfigAdmin(ModelAdmin):
    inlines = [SlideInline]
    list_display = ["generation", "president", "vice_president"]

    def save_related(self, request, form, formsets, change):
        print(form)

        return super().save_related(request, form, formsets, change)


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
