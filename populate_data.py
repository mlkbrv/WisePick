#!/usr/bin/env python
"""
Скрипт для заполнения базы данных тестовыми данными
"""
import os
import sys
import django

# Настройка Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WisePick.settings')
django.setup()

from core.models import CPU, GPU, RAM, Needs

def create_cpus():
    """Создает тестовые данные для CPU"""
    cpus_data = [
        {
            'name': 'Intel Core i7-12700K',
            'clock_speed_ghz': 3.6,
            'core_count': 12,
            'thread_count': 20,
            'cache_size_l1': 384,
            'cache_size_l2': 12288,
            'cache_size_l3': 25600,
            'tdp_watts': 125,
            'architecture_generation': 'Alder Lake',
            'ipc': 1.2
        },
        {
            'name': 'AMD Ryzen 7 5800X',
            'clock_speed_ghz': 3.8,
            'core_count': 8,
            'thread_count': 16,
            'cache_size_l1': 512,
            'cache_size_l2': 4096,
            'cache_size_l3': 32768,
            'tdp_watts': 105,
            'architecture_generation': 'Zen 3',
            'ipc': 1.1
        },
        {
            'name': 'Intel Core i5-12400F',
            'clock_speed_ghz': 2.5,
            'core_count': 6,
            'thread_count': 12,
            'cache_size_l1': 192,
            'cache_size_l2': 6144,
            'cache_size_l3': 18432,
            'tdp_watts': 65,
            'architecture_generation': 'Alder Lake',
            'ipc': 1.0
        },
        {
            'name': 'AMD Ryzen 5 5600X',
            'clock_speed_ghz': 3.7,
            'core_count': 6,
            'thread_count': 12,
            'cache_size_l1': 384,
            'cache_size_l2': 3072,
            'cache_size_l3': 32768,
            'tdp_watts': 65,
            'architecture_generation': 'Zen 3',
            'ipc': 1.1
        }
    ]
    
    for cpu_data in cpus_data:
        cpu, created = CPU.objects.get_or_create(
            name=cpu_data['name'],
            defaults=cpu_data
        )
        if created:
            print(f"Created CPU: {cpu.name}")
        else:
            print(f"CPU already exists: {cpu.name}")

def create_gpus():
    """Создает тестовые данные для GPU"""
    gpus_data = [
        {
            'name': 'NVIDIA RTX 4080',
            'vram_gb': 16.0,
            'core_count': 9728,
            'core_clock_ghz': 2.21,
            'memory_bandwidth_gbps': 716.8,
            'architecture': 'Ada Lovelace',
            'ray_tracing_support': True,
            'release_year': 2022
        },
        {
            'name': 'NVIDIA RTX 4070',
            'vram_gb': 12.0,
            'core_count': 5888,
            'core_clock_ghz': 1.92,
            'memory_bandwidth_gbps': 504.2,
            'architecture': 'Ada Lovelace',
            'ray_tracing_support': True,
            'release_year': 2023
        },
        {
            'name': 'AMD Radeon RX 7800 XT',
            'vram_gb': 16.0,
            'core_count': 3840,
            'core_clock_ghz': 2.12,
            'memory_bandwidth_gbps': 624.0,
            'architecture': 'RDNA 3',
            'ray_tracing_support': True,
            'release_year': 2023
        },
        {
            'name': 'NVIDIA RTX 3060',
            'vram_gb': 12.0,
            'core_count': 3584,
            'core_clock_ghz': 1.32,
            'memory_bandwidth_gbps': 360.0,
            'architecture': 'Ampere',
            'ray_tracing_support': True,
            'release_year': 2021
        }
    ]
    
    for gpu_data in gpus_data:
        gpu, created = GPU.objects.get_or_create(
            name=gpu_data['name'],
            defaults=gpu_data
        )
        if created:
            print(f"Created GPU: {gpu.name}")
        else:
            print(f"GPU already exists: {gpu.name}")

def create_rams():
    """Создает тестовые данные для RAM"""
    rams_data = [
        {
            'name': 'Corsair Vengeance LPX 32GB DDR4-3200',
            'size_gb': 32,
            'speed_mhz': 3200,
            'type': 'DDR4'
        },
        {
            'name': 'G.Skill Ripjaws V 16GB DDR4-3600',
            'size_gb': 16,
            'speed_mhz': 3600,
            'type': 'DDR4'
        },
        {
            'name': 'Corsair Dominator Platinum 64GB DDR5-5600',
            'size_gb': 64,
            'speed_mhz': 5600,
            'type': 'DDR5'
        },
        {
            'name': 'G.Skill Trident Z5 32GB DDR5-6000',
            'size_gb': 32,
            'speed_mhz': 6000,
            'type': 'DDR5'
        }
    ]
    
    for ram_data in rams_data:
        ram, created = RAM.objects.get_or_create(
            name=ram_data['name'],
            defaults=ram_data
        )
        if created:
            print(f"Created RAM: {ram.name}")
        else:
            print(f"RAM already exists: {ram.name}")

def create_needs():
    """Создает тестовые данные для Needs"""
    needs_data = [
        {
            'name': 'gaming',
            'description': 'High-performance gaming with modern AAA titles'
        },
        {
            'name': 'work',
            'description': 'General office work, web browsing, and productivity'
        },
        {
            'name': 'video_editing',
            'description': 'Professional video editing and content creation'
        },
        {
            'name': '3d_rendering',
            'description': '3D modeling, rendering, and CAD work'
        }
    ]
    
    for need_data in needs_data:
        need, created = Needs.objects.get_or_create(
            name=need_data['name'],
            defaults=need_data
        )
        if created:
            print(f"Created Need: {need.name}")
        else:
            print(f"Need already exists: {need.name}")

def main():
    """Основная функция для заполнения базы данных"""
    print("Starting database population...")
    
    print("\nCreating CPUs...")
    create_cpus()
    
    print("\nCreating GPUs...")
    create_gpus()
    
    print("\nCreating RAM modules...")
    create_rams()
    
    print("\nCreating Needs...")
    create_needs()
    
    print("\nDatabase population completed!")
    print(f"Total CPUs: {CPU.objects.count()}")
    print(f"Total GPUs: {GPU.objects.count()}")
    print(f"Total RAM modules: {RAM.objects.count()}")
    print(f"Total Needs: {Needs.objects.count()}")

if __name__ == '__main__':
    main()
