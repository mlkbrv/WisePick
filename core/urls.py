from django.urls import path, include
from . import views

urlpatterns = [
    path("cpu/", views.CPUListCreateAPIView.as_view(), name="cpu-list-create"),
    path("cpu/<int:pk>", views.CPUDetailAPIView.as_view(), name="cpu-detail"),
    path("compare_cpu/<str:cpu1>/<str:cpu2>", views.CPUCompareAPIView.as_view(), name="cpu-compare-list-create"),
    path("gpu/", views.GPUListCreateAPIView.as_view(), name="gpu-list-create"),
    path("gpu/<int:pk>", views.GPUDetailAPIView.as_view(), name="gpu-detail"),
    path("compare_gpu/<str:gpu1>/<str:gpu2>", views.GPUCompareAPIView.as_view(), name="gpu-compare-list-create"),
    path("ram/", views.RAMListCreateAPIView.as_view(), name="ram-list-create"),
    path("ram/<int:pk>", views.RAMDetailAPIView.as_view(), name="ram-detail"),
    path("compare_ram/<str:ram1>/<str:ram2>", views.RAMCompareAPIView.as_view(), name="ram-compare-list-create"),
    path("needs/", views.NeedsListCreateAPIView.as_view(), name="needs-list-create"),
    path("needs/<int:pk>", views.NeedsDetailAPIView.as_view(), name="needs-detail"),
    path("compare_pc/<str:cpu1>/<str:gpu1>/<str:ram1>/<str:cpu2>/<str:gpu2>/<str:ram2>/<str:need>", views.NeedsCompareAPIView.as_view(), name="needs-compare"),
]
