from django.urls import path, include
from . import views
urlpatterns = [
    path("cpu/",views.CPUListCreateAPIView.as_view(), name="cpu-list-create"),
    path("cpu/<int:pk>",views.CPUDetailAPIView.as_view(), name="cpu-detail"),
    path("compare_cpu/<str:cpu1>/<str:cpu2>", views.CPUCompareAPIView.as_view(), name="cpu-compare-list-create"),
    path("gpu/",views.GPUListCreateAPIView.as_view(), name="gpu-list-create"),
    path("gpu/<int:pk>",views.GPUDetailAPIView.as_view(), name="gpu-detail"),
    path("compare_gpu/<str:gpu1>/<str:gpu2>", views.GPUCompareAPIView.as_view(), name="gpu-compare-list-create")

]