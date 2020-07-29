from django.urls import path
from . import views

urlpatterns = [
    path('',views.student_list, name='home'),
    path('api/', views.StudentCRUDView.as_view()),
]