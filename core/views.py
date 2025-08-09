from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .ai import *
from .models import *
from .serializers import CPUSerializer, GPUSerializer, RAMSerializer, NeedsSerializer
import urllib.parse


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
    serializer_class = RAMSerializer


class RAMDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer


class RAMCompareAPIView(APIView):
    def get(self, request, ram1, ram2):
        data = get_ram_comparison_json(ram1, ram2)
        if data is None:
            return Response({"error": "Failed to compare RAMs"}, status=400)
        return Response(data)


class NeedsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Needs.objects.all()
    serializer_class = NeedsSerializer


class NeedsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Needs.objects.all()
    serializer_class = NeedsSerializer


class NeedsCompareAPIView(APIView):
    def get(self, request, cpu1, gpu1, ram1, cpu2, gpu2, ram2, need):
        # Decode URL-encoded parameters
        cpu1 = urllib.parse.unquote(cpu1)
        gpu1 = urllib.parse.unquote(gpu1)
        ram1 = urllib.parse.unquote(ram1)
        cpu2 = urllib.parse.unquote(cpu2)
        gpu2 = urllib.parse.unquote(gpu2)
        ram2 = urllib.parse.unquote(ram2)
        need = urllib.parse.unquote(need)
        
        # Form components for comparison
        pc1_components = {
            'cpu_name': cpu1,
            'gpu_name': gpu1,
            'ram_name': ram1
        }
        
        pc2_components = {
            'cpu_name': cpu2,
            'gpu_name': gpu2,
            'ram_name': ram2
        }
        
        # Call comparison function
        data = get_pc_comparison_json(pc1_components, pc2_components, need)
        if data is None:
            return Response({"error": "Failed to compare PC configurations"}, status=400)
        return Response(data)
