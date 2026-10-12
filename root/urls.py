from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app.views import RegisterView, LogoutView, MeView, VerifyEmailView, ResendCodeView, ForgotPasswordView, \
    ConfirmPasswordView, ResetPasswordView

schema_view = get_schema_view(
    openapi.Info(
        title="Radifus API",
        default_version='v1',
        description="0 dan boshlab oxirigacha",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("user/register/", RegisterView.as_view()),
    path("user/login/", TokenObtainPairView.as_view()),
    path("user/refresh/", TokenRefreshView.as_view()),
    path("user/logout/", LogoutView.as_view()),
    path("me/", MeView.as_view()),
    path("user/verify-email/", VerifyEmailView.as_view()),
    path("user/resend-code/", ResendCodeView.as_view()),

    path("forgot/forgot-password/", ForgotPasswordView.as_view()),
    path("forgot/confirm-password/", ConfirmPasswordView.as_view()),
    path("forgot/reset-password/", ResetPasswordView.as_view()),
]
