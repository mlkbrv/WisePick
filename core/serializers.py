from rest_framework import serializers
from .models import CPU, GPU, RAM, Needs

class NeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Needs
        fields = '__all__'

class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = '__all__'


class GPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPU
        fields = '__all__'


class RAMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAM
        fields = '__all__'
