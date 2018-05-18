from django.urls import path
from . import views


urlpatterns = [
    path('users/<int:i>', views.UserList.as_view(), name='user-list'),
    path('users/<int:iw>', views.UserDetail.as_view(), name='user-detail'),
]