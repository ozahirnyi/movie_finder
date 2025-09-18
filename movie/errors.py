from rest_framework import status
from rest_framework.exceptions import APIException


class AddLikeError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'THE_MOVIE_IS_LIKED'
    default_detail = 'User has already liked this movie'
