from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from users import views
 
 
urlpatterns = [
    path('users/$', views.UserList.as_view(), name='user-list'),
    path('users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),