from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CPU
from .serializers import CPUSerializer

class CPUListCreateAPIView(generics.ListCreateAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer

class CPUDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer

from .ai import *

class CompareAPIView(APIView):
    def get(self, request, cpu1, cpu2):
        data = get_cpu_comparison_json(cpu1, cpu2)
        if data is None:
            return Response({"error": "Failed to compare processors"}, status=400)
        return Response(data)