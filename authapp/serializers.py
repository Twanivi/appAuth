from rest_framework import serializers
class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)


class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ConfirmForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    verification_code = serializers.CharField()
    new_password = serializers.CharField(max_length=8)
