from django.db import models


class Job(models.Model):
    """
    Kasb uchun model
    """
    title = models.CharField(max_length=50)
    salary = models.PositiveIntegerField(default=0)
    added_at = models.DateTimeField(auto_now=True)
