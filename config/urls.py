"""
URL configuration for xOneProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView

from src.users.views import LogoutAPIView, LoginAPIView, RegisterAPIView, EmailVerify, ChangePasswordAPIView, \
    ForgotPasswordAPIView, RecoverPasswordAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/change-password/', ChangePasswordAPIView.as_view(), name='change_password'),
    path('api/v1/forgot-password/', ForgotPasswordAPIView.as_view(),  name='forgot_password'),
    path('api/v1/recover-password/', RecoverPasswordAPIView.as_view(),  name='forgot_password'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/logout/', LogoutAPIView.as_view(), name='logging_out'),
    path('api/v1/login/', LoginAPIView.as_view(), name='logging_in'),
    path('api/v1/register/', RegisterAPIView.as_view(), name="sign_up"),
    path('api/v1/verify-email/', EmailVerify.as_view(), name='verify_email'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
]
