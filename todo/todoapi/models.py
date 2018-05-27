from django.db import models

class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    user = models.ForeignKey('users.User', related_name='todoapi', on_delete=models.CASCADE, null=False)
 
    class Meta:
      ordering = ('created',)
