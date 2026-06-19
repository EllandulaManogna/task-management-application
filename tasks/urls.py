from django.urls import path
from . import views

urlpatterns = [

    path('dashboard/', views.dashboard, name='dashboard'),

    path(
        'complete/<int:id>/',
        views.complete_task,
        name='complete_task'
    ),

    path(
        'delete/<int:id>/',
        views.delete_task,
        name='delete_task'
    ),

    path(
        'edit/<int:id>/',
        views.edit_task,
        name='edit_task'
    ),
]