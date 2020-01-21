from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>/',views.teacher),
    path('<int:id>/addassignment/',views.addAssignment),
    path('<int:id>/addassignment/<str:topic>/',views.addQuetions),
    path('<int:id>/assignmentstatus',views.assignmentStatus),
    path('<int:id>/assignmentstatus/<str:topic>',views.status),
    path('logout',views.logout),
]