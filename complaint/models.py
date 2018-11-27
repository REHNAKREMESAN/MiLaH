from django.db import models
from lab_reg.models import LabReg
from datetime import date

class Complaint(models.Model):
    contractor_id = models.BigIntegerField()
    employee_name = models.ForeignKey(LabReg, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default='')
    complaint_date = models.DateField(default=date.today)
    complaint_status = models.CharField(max_length=10, default='')
    complaint_reply = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.employee_name

