from django.contrib import admin
from .models import Complaint


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ["contractor_id",  "employee_name", "description", "complaint_date", "complaint_status", "complaint_reply"]


admin.site.register(Complaint, ComplaintAdmin)
