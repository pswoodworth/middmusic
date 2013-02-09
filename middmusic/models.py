from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings
from django.forms import ModelForm


class Band(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=3000)
	photo = models.FileField(upload_to="img/"+str(timezone.now()), blank=True, null=True)
	email = models.EmailField(max_length=100, blank=True, null=True)
	website = models.URLField(max_length=200, blank=True, null=True)
	PIN = models.PositiveIntegerField(max_length=4)
	def __unicode__(self):
		return self.name

class Event(models.Model):
	name = models.CharField(max_length=200)
	date = models.DateTimeField('event date')
	description = models.TextField(max_length=3000)
	photo = models.FileField(upload_to="img/"+str(timezone.now()), blank=True, null=True)
	email = models.EmailField(max_length=100, blank = True, null=True)
	website = models.URLField(max_length=200, blank = True, null=True)
	PIN = models.PositiveIntegerField(max_length=4)
	def __unicode__(self):
		return self.name
	def is_today(self):
		return (timezone.now()-timezone.timedelta(hours=5)).date() == (self.date-timezone.timedelta(hours=5)).date()
	def is_tomorrow(self):
		return (self.date-timezone.timedelta(hours=5)).date() == (timezone.now()-timezone.timedelta(hours=5)).date() + timezone.timedelta(days=1)
	def is_passed(self):
		return (self.date - timezone.now()) < datetime.timedelta(hours=-6)

class Classified(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=3000)
	email = models.EmailField(max_length=100)
	website = models.URLField(max_length=200, blank=True, null=True)
	post_date = models.DateTimeField('post date', auto_now=True)
	PIN = models.PositiveIntegerField(max_length=4)
	def __unicode__(self):
		return self.title

class FAQ(models.Model):
	question = models.CharField(max_length=500)
	answer = models.TextField(max_length=3000)


class BandForm(ModelForm):
	class Meta:
		model = Band

class EventForm(ModelForm):
	class Meta:
		model = Event

class ClassifiedForm(ModelForm):
	class Meta:
		model = Classified
