"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from todo.views import api_root
from users.views import UserList, UserDetail
from todoapi.views import TodoList, TodoDetail

router = routers.DefaultRouter()
router.register('users', UserList)
router.register('users', UserDetail)
router.register('todoapi', TodoList)
router.register('todoapi', TodoDetail)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Todo API', description='RESTful API for Todo')),
    path('', api_root),
    path('users/', include('users.urls', namespace='users')),
    path('todoapi/', include('todoapi.urls', namespace='todoapi')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
