from django.contrib import admin
from .models import Workout,Exercise
# Register your models here.

class WorkoutAdmin(admin.ModelAdmin):
  search_fields = ["pk","date"]
  list_filter = ["date"]
  list_display = ["pk","date","Workout_for","no_of_set"]
admin.site.register(Workout,WorkoutAdmin)
admin.site.register(Exercise)