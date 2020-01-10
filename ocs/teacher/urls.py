from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>/',views.teacher),
    path('<int:id>/addassignment/',views.addAssignment),
]