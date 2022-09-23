from rest_framework import status
from rest_framework.exceptions import APIException


class FindMovieNotExist(APIException):
    status_code = status.HTTP_204_NO_CONTENT
    default_code = 'FIND_MOVIE_NOT_EXIST'
    default_detail = 'Find movie not exist'


class AddLikeError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = 'THE_MOVIE_IS_LIKED'
    default_detail = 'The user has already liked this movie'
