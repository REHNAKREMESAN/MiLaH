from django.db import models


class AddStatus(models.Model):
    status = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.chit_name

