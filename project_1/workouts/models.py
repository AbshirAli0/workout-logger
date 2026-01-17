from django.db import models
from django.conf import settings

# Create your models here.

class Workout(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="workouts"
    )

    def __str__(self):
        return f"Workout by {self.user}"

    
