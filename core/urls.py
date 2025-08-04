from django.urls import path, include
from . import views
urlpatterns = [
    path("cpu/",views.CPUListCreateAPIView.as_view(), name="cpu-list-create"),
    path("cpu/<int:pk>",views.CPUDetailAPIView.as_view(), name="cpu-detail"),
]