from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class project(models.Model):
	name        = models.CharField(max_length=250)
	description = models.CharField(max_length=250)
	
	start       = models.DateField()
	end         = models.DateField()
	
	owner       = models.ForeignKey(User,related_name='Owner User')
	date        = models.DateField(auto_now_add=True)
	class Meta:
		verbose_name        = 'Project'
		verbose_name_plural = 'Projects'
	def __unicode__(self):
		return "%s" % self.name



class information_general(models.Model):
	project = models.ForeignKey(project, unique=True)
	name = models.CharField(max_length=250)
	date = models.DateField(auto_now_add=True)
	class Meta:
		verbose_name = 'Information General'
		verbose_name_plural = 'Information General of projects'
	def __unicode__(self):
		return "%s" % self.name
    

 