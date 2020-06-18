from django.contrib import admin
from .models import Workout,Exercise,Bmi,Bmr
# Register your models here.

class WorkoutAdmin(admin.ModelAdmin):
  search_fields = ["pk","date"]
  list_filter = ["date"]
  list_display = ["pk","date","Workout_for","no_of_set","name"]
  def name(self,obj):
    return obj.user.first_name+' '+obj.user.last_name

class ExserciseAdmin(admin.ModelAdmin):
  list_filter = ["workout"]
  list_display = [
    "pk",
    "exercise",
    "repeatation",
    "workout"
  ]
class BmrAdmin(admin.ModelAdmin):
  list_display = [
    "pk",
    "name",
    "bmr",
    "date_filled",
  ]
  def name(self,obj):
    return obj.user.first_name+" "+obj.user.last_name

class BmiAdmin(admin.ModelAdmin):
  list_display = [
    "pk",
    "name",
    "bmi",
    "date_checked",
  ]
  def name(self,obj):
    return obj.user.first_name+" "+obj.user.last_name

admin.site.register(Workout,WorkoutAdmin)
admin.site.register(Exercise,ExserciseAdmin)
admin.site.register(Bmr,BmrAdmin)
admin.site.register(Bmi,BmiAdmin)