from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add',views.addWorkout,name='add_workout'),
    path('add_exercise/<int:id>',views.addExersice,name='add_exercise'),
    path('disp',views.dispData,name="disp"),
    path('update/<int:id>',views.updateData,name="update"),
    path('update_exersice/<int:id>',views.updateExersice,name='update_exersice'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('logout',views.userLogout,name='logout'),
    path('login',views.userLogin,name='login'),
    path('signup',views.userSingup,name='signup'),
    path('bmr_calculator',views.bmrCalculator,name="bmr_calculator"),
    path('bmr_submit',views.bmrSubmit,name="bmr_submit"),
    path('bmi_calculator',views.bmiCalculator,name="bmi_calculator"),
    path('bmi_submit',views.bmiSubmit,name="bmi_submit"),
    path('stopwatch',views.stopwatch,name="stopwatch"),
]