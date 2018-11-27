from django.db import models
from state.models import State
from district.models import District
from security_question.models import Security_question


CHOICES = [('male', 'Male'), ('female', 'Female'), ('others', 'Others')]


class ContractorReg(models.Model):
    contractor_name = models.CharField(max_length=20, default='')
    house_name = models.CharField(max_length=20, default='')
    street = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')
    contact = models.BigIntegerField(default='')
    email = models.EmailField(max_length=30, default='')
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    gender = models.CharField(choices=CHOICES, max_length=10)
    licence = models.BigIntegerField(default='')
    username = models.CharField(max_length=20, default='')
    password = models.CharField(max_length=20, default='')
    security_question = models.ForeignKey(Security_question, on_delete=models.CASCADE)
    security_answer = models.CharField(max_length=20, default='')
    status = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.contractor_name
