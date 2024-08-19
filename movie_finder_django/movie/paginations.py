from rest_framework import pagination


class MoviesPagination(pagination.LimitOffsetPagination):
    default_limit = 12
    max_limit = 100
