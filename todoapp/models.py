from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
	STATUS_CHOICES = (
		('active', 'Active'),
		('completed', 'Completed'),
	)
	title = models.CharField(max_length=50)
	created_by = models.ForeignKey(User, related_name='todo_apps')
	completed = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='active')

	def get_absolute_url(self):
		return reverse('todoapp:todo_detail', args=[self.id])

	def __str__(self):
		return self.title