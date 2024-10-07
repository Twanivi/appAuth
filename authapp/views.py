from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .cognito import sign_up, sign_in, forgot_password, confirm_forgot_password
from .serializers import SignUpSerializer, SignInSerializer, ForgotPasswordSerializer, ConfirmForgotPasswordSerializer

class SignUpAPIView(generics.CreateAPIView):
    serializer_class = SignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = sign_up(serializer.validated_data['email'], serializer.validated_data['password'])
        return Response(response, status=status.HTTP_201_CREATED)


class SignInAPIView(generics.CreateAPIView):
    serializer_class = SignInSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = sign_in(serializer.validated_data['email'], serializer.validated_data['password'])
        return Response(response, status=status.HTTP_200_OK)


class ForgotPasswordAPIView(generics.CreateAPIView):
    serializer_class = ForgotPasswordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = forgot_password(serializer.validated_data['email'])
        return Response(response, status=status.HTTP_200_OK)


class ConfirmForgotPasswordAPIView(generics.CreateAPIView):
    serializer_class = ConfirmForgotPasswordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = confirm_forgot_password(
            serializer.validated_data['email'],
            serializer.validated_data['verification_code'],
            serializer.validated_data['new_password']
        )
        return Response(response, status=status.HTTP_200_OK)
