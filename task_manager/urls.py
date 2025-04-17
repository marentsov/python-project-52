"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path


from task_manager.views import IndexView, index
from users.views import UserLoginView, UserLogoutView
app_name = 'main'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('testrollbar/', index, name='test'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('users/', include('users.urls', namespace='users')),
    path('statuses/', include('statuses.urls', namespace='statuses')),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('labels/', include('labels.urls', namespace='labels')),
]
