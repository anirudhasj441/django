from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>/',views.teacher),
    path('addassignment/',views.addAssignment),
]