from django.urls import path
from . import views

app_name='todoapi'
urlpatterns = [
    path('todoapi/', views.TodoList.as_view(), name='todo-list'),
    path('todoapi/<int:pk>/', views.TodoDetail.as_view(), name='todo-detail'),
]
