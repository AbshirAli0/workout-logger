from django.contrib import admin
from .models import Workout

# Register your models here.

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("exercise","weight","sets", "reps", "created_at",)
    search_fields = ("exercise",)
    list_filter = ("created_at",)
    


