from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .ai import *
from .models import *
from .serializers import CPUSerializer, GPUSerializer


class CPUListCreateAPIView(generics.ListCreateAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer


class CPUDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer


class CPUCompareAPIView(APIView):
    def get(self, request, cpu1, cpu2):
        data = get_cpu_comparison_json(cpu1, cpu2)
        if data is None:
            return Response({"error": "Failed to compare processors"}, status=400)
        return Response(data)


class GPUListCreateAPIView(generics.ListCreateAPIView):
    queryset = GPU.objects.all()
    serializer_class = GPUSerializer


class GPUDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GPU.objects.all()
    serializer_class = GPUSerializer


class GPUCompareAPIView(APIView):
    def get(self, request, gpu1, gpu2):
        data = get_gpu_comparison_json(gpu1, gpu2)
        if data is None:
            return Response({"error": "Failed to compare video cards"}, status=400)
        return Response(data)


class RAMListCreateAPIView(generics.ListCreateAPIView):
    queryset = RAM.objects.all()
    serializer_class = GPUSerializer


class RAMDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RAM.objects.all()
    serializer_class = GPUSerializer


class RAMCompareAPIView(APIView):
    def get(self, request, ram1, ram2):
        data = get_gpu_comparison_json(ram1, ram2)
        if data is None:
            return Response({"error": "Failed to compare RAMs"}, status=400)
        return Response(data)
