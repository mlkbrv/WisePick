from django.shortcuts import render
from rest_framework import generics
from .models import CPU
from .serializers import CPUSerializer

class CPUListCreateAPIView(generics.ListCreateAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer

class CPUDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer