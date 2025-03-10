from django.db import models
from datetime import date

class Task(models.Model):
    STATUS_CHOICES = [
        ('UPCOMING', 'Upcoming'),
        ('DUE TODAY', 'Due Today'),
        ('OVERDUE', 'Overdue'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='UPCOMING')

    def save(self, *args, **kwargs):
        today = date.today()
        if self.due_date < today:
            self.status = 'OVERDUE'
        elif self.due_date == today:
            self.status = 'DUE TODAY'
        else:
            self.status = 'UPCOMING'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
