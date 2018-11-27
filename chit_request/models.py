from django.db import models
from chit.models import Chit


class ChitRequest(models.Model):
    chit_name = models.ForeignKey(Chit, on_delete=models.CASCADE)
    members_name = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.members_name

