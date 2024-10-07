from django.urls import path
from .views import SignUpAPIView, SignInAPIView, ForgotPasswordAPIView, ConfirmForgotPasswordAPIView

urlpatterns = [
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('signin/', SignInAPIView.as_view(), name='signin'),
    path('forgot-password/', ForgotPasswordAPIView.as_view(), name='forgot_password'),
    path('confirm-forgot-password/', ConfirmForgotPasswordAPIView.as_view(), name='confirm_forgot_password')
]
