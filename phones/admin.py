from django.contrib import admin

from phones.models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        '__str__'
    )
    # search_fields = ['id']
    # list_filter = (
    # )
    pass
