from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

# Create your models here.

class getda(models.Model):
	a = models.TextField(null = False, blank = False)

class getForm(ModelForm):
	class Meta:
		model = getda
		fields = '__all__'

