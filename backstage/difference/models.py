from django.db import models

class DifferenceN(models.Model):
    n = models.IntegerField(primary_key=True, default=0)
    value = models.IntegerField(default=0)
    occurences = models.IntegerField(default=0)

class SeqABC(models.Model):
	a = models.IntegerField()
	b = models.IntegerField()
	c = models.IntegerField()
	pythagorean_triple = models.BooleanField(default=False)
	seq_sum = models.IntegerField(default=0)
	occurences = models.IntegerField(default=0)

	class Meta:
		unique_together = ('a', 'b', 'c')