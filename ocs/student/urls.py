from django.urls import path
from . import views
urlpatterns = [
    path('<int:pnr>/',views.student),
    path('<int:pnr>/assignment/',views.assignment),
    path('<int:pnr>/assignment/<str:topic>/',views.questions),
    path('<int:pnr>/assignment/<str:topic>/result/',views.result),
]