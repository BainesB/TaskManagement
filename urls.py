from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/', views.mark_completed, name='mark_completed'),
    path('pending/<int:task_id>/', views.mark_pending, name='mark_pending'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
