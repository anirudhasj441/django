from django.contrib import admin
from .models import Assigments,AssignmentDate,SolvedAssignments
# Register your models here.
admin.site.register(Assigments)
admin.site.register(AssignmentDate)
admin.site.register(SolvedAssignments)