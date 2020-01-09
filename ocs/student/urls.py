from django.urls import path
from . import views
urlpatterns = [
    path('<int:pnr>',views.student),
]