from rest_framework.pagination import PageNumberPagination

class CPUPagination(PageNumberPagination):
    page_size = 20

class GPUPagination(PageNumberPagination):
    page_size = 20

class RAMPagination(PageNumberPagination):
    page_size = 20

class NeedsPagination(PageNumberPagination):
    page_size = 5