from rest_framework import serializers
from .models import CPU

class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = '__all__'
