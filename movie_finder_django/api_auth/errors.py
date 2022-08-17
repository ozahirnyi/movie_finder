from rest_framework import status
from rest_framework.exceptions import APIException


class UserAlreadyExist(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_code = 'USER_ALREADY_EXIST'
    default_detail = 'User already exist'
