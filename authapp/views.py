import boto3
from botocore.exceptions import ClientError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from .serializers import SignUpSerializer, SignInSerializer, ForgotPasswordSerializer, ConfirmForgotPasswordSerializer

class SignUpAPIView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            client = boto3.client('cognito-idp', region_name=settings.AWS_REGION)

            try:
                response = client.sign_up(
                    ClientId=settings.COGNITO_CLIENT_ID,
                    Username=email,
                    Password=password,
                    UserAttributes=[{'Name': 'email', 'Value': email}]
                )
                return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
            except ClientError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignInAPIView(APIView):
    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            client = boto3.client('cognito-idp', region_name=settings.AWS_REGION)

            try:
                response = client.initiate_auth(
                    ClientId=settings.COGNITO_CLIENT_ID,
                    AuthFlow='USER_PASSWORD_AUTH',
                    AuthParameters={
                        'USERNAME': email,
                        'PASSWORD': password
                    }
                )
                return Response({'message': 'Login successful',
                                 'token': response['AuthenticationResult']['AccessToken']}, status=status.HTTP_200_OK)
            except ClientError as e:
                return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForgotPasswordAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            client = boto3.client('cognito-idp', region_name=settings.AWS_REGION)

            try:
                response = client.forgot_password(
                    ClientId=settings.COGNITO_CLIENT_ID,
                    Username=email,
                )
                return Response({'message': 'Password reset code sent'}, status=status.HTTP_200_OK)
            except ClientError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmForgotPasswordAPIView(APIView):
    def post(self, request):
        serializer = ConfirmForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            verification_code = serializer.validated_data['verification_code']
            new_password = serializer.validated_data['new_password']

            client = boto3.client('cognito-idp', region_name=settings.AWS_REGION)

            try:
                response = client.confirm_forgot_password(
                    ClientId=settings.COGNITO_CLIENT_ID,
                    Username=email,
                    ConfirmationCode=verification_code,
                    Password=new_password,
                )
                return Response({'message': 'Password has been reset'}, status=status.HTTP_200_OK)
            except ClientError as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
