from __future__ import unicode_literals

from django.db import models

# Create your models here.
def user_path(instance,filename):
	return str(instance.song_url)+'/'+filename

class Data(models.Model):
	file = models.FileField(upload_to=user_path,blank=False,null=False)
	song_url = models.URLField(max_length=100,blank=False,null=False)
	user_url = models.URLField(max_length=100,blank=True,null=False)
	follow_user = models.BooleanField()