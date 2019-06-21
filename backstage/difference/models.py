from django.db import models

class DifferenceN(models.Model):
    n = models.IntegerField(primary_key=True, default=0)
    value = models.IntegerField(default=0)
    occurences = models.IntegerField(default=0)