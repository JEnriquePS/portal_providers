from django.contrib import admin

from applications.providers.models import Provider, Partnership


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Provider._meta.fields]


@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Partnership._meta.fields]
