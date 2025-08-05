from django.urls import path, include
from . import views
urlpatterns = [
    path("cpu/",views.CPUListCreateAPIView.as_view(), name="cpu-list-create"),
    path("cpu/<int:pk>",views.CPUDetailAPIView.as_view(), name="cpu-detail"),
    path("compare/<str:cpu1>/<str:cpu2>", views.CompareAPIView.as_view(), name="compare-list-create")

]