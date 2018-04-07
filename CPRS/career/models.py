# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cusers(models.Model):
	uid = models.IntegerField(null=True)
	q1 = models.CharField(max_length=255)
	q2 = models.CharField(max_length=255)
	q3 = models.CharField(max_length=255)
	q4 = models.CharField(max_length=255)
	q5 = models.CharField(max_length=255)
	q6 = models.CharField(max_length=255)
	q7 = models.CharField(max_length=255)
	q8 = models.CharField(max_length=255)
	q9 = models.CharField(max_length=255)
	q10 = models.CharField(max_length=255)
	q11 = models.CharField(max_length=255)
	q12 = models.CharField(max_length=255)
	q13 = models.CharField(max_length=255)
	q14 = models.CharField(max_length=255)
	q15 = models.CharField(max_length=255)
	
	def __str__(self):
		return str(self.uid)