from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class PageLimitPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10

class PagePagination(PageNumberPagination):
    page_size = 2
    max_page_size = 10