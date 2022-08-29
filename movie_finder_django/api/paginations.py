from rest_framework import pagination


class MoviesPagination(pagination.LimitOffsetPagination):
    default_limit = 2
    max_limit = 100
