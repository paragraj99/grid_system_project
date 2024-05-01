from django.urls import path
from . import views

urlpatterns = [
    path('student_list/',views.student_list,name='student_list'),
]


# main 
# http://127.0.0.1:8000/students/student_list/  