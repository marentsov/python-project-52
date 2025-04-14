from django.urls import path
from users import views

app_name = 'users'


urlpatterns = [
    path('', views.UserListView.as_view(), name='users'),
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('<int:id>/update/', views.UserUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='delete'),
    path('logout/', views.logout, name='logout'),
]
