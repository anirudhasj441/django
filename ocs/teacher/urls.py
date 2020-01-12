from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>/',views.teacher),
    path('<int:id>/addassignment/',views.addAssignment),
    path('<int:id>/addassignment/<str:topic>/',views.addQuetions),
]