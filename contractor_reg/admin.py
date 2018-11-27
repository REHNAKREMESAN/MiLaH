from django.contrib import admin
from .models import ContractorReg


class ContractorRegAdmin(admin.ModelAdmin):
    list_display = ["contractor_name",  "house_name", "street", "city", "contact", "email", "state", "district",
                    "gender", "licence", "username", "password", "security_question", "security_answer", "status"]


admin.site.register(ContractorReg, ContractorRegAdmin)
