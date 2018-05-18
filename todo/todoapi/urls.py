from django.urls import path
from . import views
 
urlpatterns = [
    path('todoapi/<int:id2>', views.TodoList.as_view(), name='todo-list'),
    path('todoapi/<int:id>', views.TodoDetail.as_view(), name='todo-detail'),
]
