from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),
    path('<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('profile/', views.CurrentUserDetail.as_view(), name='user-profile'),
]

