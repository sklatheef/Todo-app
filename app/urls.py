from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('display/', views.display, name='display'),
    path('task/<int:id>/', views.single, name='single'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
    path('history/', views.history, name='history'), 
    path('restore/<int:id>/', views.restore_task, name='restore_task'), # New route
    path('about/', views.about, name='about'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:id>/', views.toggle_status, name='toggle_status'),
]
