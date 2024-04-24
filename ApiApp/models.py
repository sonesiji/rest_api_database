from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Language(models.Model):
    STATUS_CHOICES = (
        ('to_learn', 'To Learn'),
        ('learned', 'Learned'),
        ('forgot', 'Forgot'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    meaning = models.TextField(max_length=255, default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_learn')
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    

    

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title