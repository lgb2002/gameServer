from django.db import models

class UserInfo(models.Model):
	name = models.ForeignKey('auth.User',on_delete=models.CASCADE)

	def __str__(self):
		return self.name