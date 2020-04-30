from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.USER', on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=1000)
	create_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
