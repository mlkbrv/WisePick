from rest_framework import serializers
from .models import CPU, GPU, RAM, Needs, Phone

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

class PhoneSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Phone
        fields = [
            'name',
            'brand',
            'image',
            'ram_size',
            'memory_size',
            'processor',
            'os_type',
            'graphic_processor',
            'camera_mp',
            'screen_type',
            'battery',
            'year'
        ]