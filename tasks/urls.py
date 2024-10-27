# In your app's urls.py
from django.urls import path

from.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, Login, RegisterPage
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import logout_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', Login.as_view(), name='login'),  # Login

    path('logout/', logout_view, name='logout'),  # Logout route
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Django's default login view
    
    path('register/', RegisterPage.as_view(), name='register'),  # Register
    path('', TaskList.as_view(), name='tasks'),  # List all tasks
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),  # Detail with PK
    path('task-create/', TaskCreate.as_view(), name='task-create'),  # Create a task
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),  # Update a task
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),  # Delete a task
] 
