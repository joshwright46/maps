from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from apps.users import views

urlpatterns = [  
    path('token/', views.EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('register-verify/<str:token>/', views.VerifyEmailView.as_view(), name='register-verify'),
    path('password-reset/', views.PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-verify/<str:uidb64>/<str:token>/', views.PasswordResetVerifyView.as_view(), name='password-reset-verify'),
]

