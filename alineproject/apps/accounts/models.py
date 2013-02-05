#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from sorl.thumbnail import ImageField



class UserProfile(models.Model):
	userType = ((1:"User"),(2:"Admin"),(3:"Super Admin"))
	user = models.ForeignKey(User, unique=True)
	user_type = models.IntegerField(default=1,choices=userType)
	image = models.ImageField(upload_to='accounts/profile',blank=True,null=True)


	def __unicode__(self):
		_user = self.user
		if _user.first_name == "":
			return _user.username
		else:
			return "%s %s"%(_user.first_name,_user.last_name) 

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)


class organization(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='organization/profile')
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = _('organization')
        verbose_name_plural = _('organizations')

    def __unicode__(self):
        return "%s" % self.name


class customer(models.Model):
	name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	company = models.CharField(max_length=250)
	email = models.EmailField()
	skype = models.CharField(max_length=100)


    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')

    def __unicode__(self):
        pass
    
    