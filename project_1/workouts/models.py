from django.db import models
from django.conf import settings

# Create your models here.

class Workout(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="workouts"
    )

    exercise = models.CharField(max_length=100)
    sets = models.IntegerField(default = 0)

    def __str__(self):
        return f"{self.exercise} by {self.user}"
    
   
    
