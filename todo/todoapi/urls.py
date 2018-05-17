from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todoapi import views
 
urlpatterns = [
    path('todoapi/$', views.TodoList.as_view(), name='todo-list'),
    path('todoapi/(?P<pk>[0-9]+)/$', views.TodoDetail.as_view(), name='todo-detail'),