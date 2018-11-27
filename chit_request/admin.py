from django.contrib import admin
from .models import ChitRequest


class ChitRequestAdmin(admin.ModelAdmin):
    list_display = ["chit_name"]


admin.site.register(ChitRequest, ChitRequestAdmin)


