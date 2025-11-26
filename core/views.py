from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .compare import *
from .ai import get_pc_comparison_json, get_phone_comparison_json
from .models import *
from .serializers import CPUSerializer, GPUSerializer, RAMSerializer, NeedsSerializer, PhoneSerializer
import urllib.parse
from .pagination import *
from rest_framework import filters

class CPUListCreateAPIView(generics.ListCreateAPIView):
    queryset = CPU.objects.order_by('pk')
    serializer_class = CPUSerializer

    pagination_class = CPUPagination

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    @method_decorator(cache_page(15,key_prefix='cpu-list-create-api-view'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class CPUDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer


class CPUCompareAPIView(APIView):

    @method_decorator(cache_page(15,key_prefix='cpu-compare-api-view'))
    def get(self, request, cpu1, cpu2):
        data = get_cpu_comparison_json(cpu1, cpu2)
        if data is None:
            return Response({"error": "Failed to compare processors"}, status=400)
        return Response(data)


class GPUListCreateAPIView(generics.ListCreateAPIView):
    queryset = GPU.objects.order_by('pk')
    serializer_class = GPUSerializer

    pagination_class = GPUPagination

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    @method_decorator(cache_page(15,key_prefix='gpu-list-create-api-view'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class GPUDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GPU.objects.all()
    serializer_class = GPUSerializer


class GPUCompareAPIView(APIView):

    @method_decorator(cache_page(15,key_prefix='gpu-compare-api-view'))
    def get(self, request, gpu1, gpu2):
        data = get_gpu_comparison_json(gpu1, gpu2)
        if data is None:
            return Response({"error": "Failed to compare video cards"}, status=400)
        return Response(data)


class RAMListCreateAPIView(generics.ListCreateAPIView):
    queryset = RAM.objects.order_by('pk')
    serializer_class = RAMSerializer

    pagination_class = RAMPagination

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    @method_decorator(cache_page(15,key_prefix='ram-list-create-api-view'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class RAMDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer


class RAMCompareAPIView(APIView):
    @method_decorator(cache_page(15,key_prefix='ram-compare-api-view'))
    def get(self, request, ram1, ram2):
        data = get_ram_comparison_json(ram1, ram2)
        if data is None:
            return Response({"error": "Failed to compare RAMs"}, status=400)
        return Response(data)


class NeedsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Needs.objects.order_by('pk')
    serializer_class = NeedsSerializer

    pagination_class = NeedsPagination

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    @method_decorator(cache_page(15,key_prefix='needs-list-create-api-view'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class NeedsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Needs.objects.all()
    serializer_class = NeedsSerializer


class NeedsCompareAPIView(APIView):

    @method_decorator(cache_page(2*60,key_prefix='needs-compare-api-view'))
    def get(self, request, cpu1, gpu1, ram1, cpu2, gpu2, ram2, need):
        cpu1 = urllib.parse.unquote(cpu1)
        gpu1 = urllib.parse.unquote(gpu1)
        ram1 = urllib.parse.unquote(ram1)
        cpu2 = urllib.parse.unquote(cpu2)
        gpu2 = urllib.parse.unquote(gpu2)
        ram2 = urllib.parse.unquote(ram2)
        need = urllib.parse.unquote(need)


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

        data = get_pc_comparison_json(pc1_components, pc2_components, need)
        if data is None:
            return Response({"error": "Failed to compare PC configurations"}, status=400)
        return Response(data)


class PhoneListCreateAPIView(generics.ListCreateAPIView):
    queryset = Phone.objects.order_by('pk')
    serializer_class = PhoneSerializer

    pagination_class = PhonePagination

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    @method_decorator(cache_page(15,key_prefix='phone-list-create-api-view'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PhoneDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class PhoneCompareAPIView(APIView):

    @method_decorator(cache_page(15,key_prefix='phone-compare-api-view'))
    def get(self, request, phone1, phone2):
        data = get_phone_comparison_json(phone1, phone2)
        if data is None:
            return Response({"error": "Failed to compare video cards"}, status=400)
        return Response(data)