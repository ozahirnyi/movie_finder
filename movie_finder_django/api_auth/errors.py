from rest_framework import status
from rest_framework.exceptions import APIException


class UserAlreadyExist(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_code = "USER_ALREADY_EXIST"
    default_detail = "User already exist"


class ChangePasswordError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "WRONG_CURRENT_PASSWORD"
    default_detail = "You entered the wrong current password"
