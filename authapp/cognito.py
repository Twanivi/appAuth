import boto3
from botocore.exceptions import ClientError

USER_POOL_ID = 'user_pool_id'
CLIENT_ID = 'app_client_id'

cognito = boto3.client('cognito-idp')

def sign_up(email, password):
    try:
        response = cognito.sign_up(
            ClientId=CLIENT_ID,
            Username=email,
            Password=password,
            UserAttributes=[{'Name': 'email', 'Value': email}]
        )
        return response
    except ClientError as e:
        return e.response['Error']['Message']

def sign_in(email, password):
    try:
        response = cognito.initiate_auth(
            ClientId=CLIENT_ID,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': email,
                'PASSWORD': password
            }
        )
        return response
    except ClientError as e:
        return e.response['Error']['Message']

def forgot_password(email):
    try:
        response = cognito.forgot_password(
            ClientId=CLIENT_ID,
            Username=email
        )
        return response
    except ClientError as e:
        return e.response['Error']['Message']

def confirm_forgot_password(email, verification_code, new_password):
    try:
        response = cognito.confirm_forgot_password(
            ClientId=CLIENT_ID,
            Username=email,
            ConfirmationCode=verification_code,
            Password=new_password
        )
        return response
    except ClientError as e:
        return e.response['Error']['Message']
