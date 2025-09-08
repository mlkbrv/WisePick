from django.db.models import Max, Min, Avg
from django.core.exceptions import ObjectDoesNotExist
import json
import os
import sys
import django
import requests
from dotenv import load_dotenv
from core.models import CPU, GPU, RAM, Needs

WEIGHTS = {
    "core_count":     0.25,
    "clock_speed":    0.20,
    "ipc":            0.30,
    "thread_count":   0.10,
    "tdp_efficiency": 0.15,
}

def _normalize(value, min_v, max_v):
    if max_v == min_v:
        return 100.0
    return 100 * (value - min_v) / (max_v - min_v)

def _build_scales():
    aggs = CPU.objects.aggregate(
        min_cc=Min("core_count"),      max_cc=Max("core_count"),
        min_cs=Min("clock_speed_ghz"), max_cs=Max("clock_speed_ghz"),
        min_ipc=Min("ipc"),            max_ipc=Max("ipc"),
        min_tc=Min("thread_count"),    max_tc=Max("thread_count"),
        min_tdp=Min("tdp_watts"),      max_tdp=Max("tdp_watts"),
    )
    return aggs

def _cpu_index(cpu: CPU, scales: dict) -> float:
    cc  = _normalize(cpu.core_count,      scales["min_cc"],  scales["max_cc"])
    cs  = _normalize(cpu.clock_speed_ghz, scales["min_cs"],  scales["max_cs"])
    ipc = _normalize(cpu.ipc,             scales["min_ipc"], scales["max_ipc"])
    tc  = _normalize(cpu.thread_count,    scales["min_tc"],  scales["max_tc"])
    tdp = 100 - _normalize(cpu.tdp_watts, scales["min_tdp"], scales["max_tdp"])

    return (cc  * WEIGHTS["core_count"]     +
            cs  * WEIGHTS["clock_speed"]    +
            ipc * WEIGHTS["ipc"]            +
            tc  * WEIGHTS["thread_count"]   +
            tdp * WEIGHTS["tdp_efficiency"])

def get_cpu_comparison_json(cpu1_name: str, cpu2_name: str):
    try:
        cpu1 = CPU.objects.get(name=cpu1_name)
        cpu2 = CPU.objects.get(name=cpu2_name)
    except ObjectDoesNotExist as e:
        return None

    scales = _build_scales()
    idx1 = _cpu_index(cpu1, scales)
    idx2 = _cpu_index(cpu2, scales)

    if idx1 > idx2:
        winner, reasoning = cpu1.name, f"{cpu1.name} wins (index {idx1:.1f} vs {idx2:.1f})"
    elif idx2 > idx1:
        winner, reasoning = cpu2.name, f"{cpu2.name} wins (index {idx2:.1f} vs {idx1:.1f})"
    else:
        winner, reasoning = "Tie", "Both CPUs show equal performance index"

    comparison = [
        {
            "name": cpu1.name,
            "clock_speed_ghz": float(cpu1.clock_speed_ghz),
            "core_count": cpu1.core_count,
            "thread_count": cpu1.thread_count,
            "tdp_watts": cpu1.tdp_watts,
            "ipc": float(cpu1.ipc),
            "performance_index": round(idx1, 2),
        },
        {
            "name": cpu2.name,
            "clock_speed_ghz": float(cpu2.clock_speed_ghz),
            "core_count": cpu2.core_count,
            "thread_count": cpu2.thread_count,
            "tdp_watts": cpu2.tdp_watts,
            "ipc": float(cpu2.ipc),
            "performance_index": round(idx2, 2),
        }
    ]

    return {
        "winner": winner,
        "reasoning": reasoning,
        "comparison": comparison
    }

GPU_WEIGHTS = {
    "core_count":            0.25,
    "core_clock":            0.20,
    "memory_bandwidth":      0.25,
    "vram":                  0.20,
    "ray_tracing":           0.10,
}

def _gpu_norm(value, min_v, max_v):
    if max_v == min_v:
        return 100.0
    return 100 * (value - min_v) / (max_v - min_v)

def _gpu_scales():
    return GPU.objects.aggregate(
        min_cc=Min("core_count"),           max_cc=Max("core_count"),
        min_ck=Min("core_clock_ghz"),       max_ck=Max("core_clock_ghz"),
        min_bw=Min("memory_bandwidth_gbps"),max_bw=Max("memory_bandwidth_gbps"),
        min_vram=Min("vram_gb"),            max_vram=Max("vram_gb"),
    )

def _gpu_index(gpu: GPU, scales: dict) -> float:
    cc  = _gpu_norm(gpu.core_count,       scales["min_cc"],   scales["max_cc"])
    ck  = _gpu_norm(gpu.core_clock_ghz,   scales["min_ck"],   scales["max_ck"])
    bw  = _gpu_norm(gpu.memory_bandwidth_gbps, scales["min_bw"], scales["max_bw"])
    vram= _gpu_norm(gpu.vram_gb,          scales["min_vram"], scales["max_vram"])
    rt  = 100.0 if gpu.ray_tracing_support else 0.0

    return (cc   * GPU_WEIGHTS["core_count"]       +
            ck   * GPU_WEIGHTS["core_clock"]       +
            bw   * GPU_WEIGHTS["memory_bandwidth"] +
            vram * GPU_WEIGHTS["vram"]             +
            rt   * GPU_WEIGHTS["ray_tracing"])

def get_gpu_comparison_json(gpu1_name: str, gpu2_name: str):
    try:
        gpu1 = GPU.objects.get(name=gpu1_name)
        gpu2 = GPU.objects.get(name=gpu2_name)
    except ObjectDoesNotExist:
        return None

    scales = _gpu_scales()
    idx1 = _gpu_index(gpu1, scales)
    idx2 = _gpu_index(gpu2, scales)

    if idx1 > idx2:
        winner, reasoning = gpu1.name, f"{gpu1.name} wins (index {idx1:.1f} vs {idx2:.1f})"
    elif idx2 > idx1:
        winner, reasoning = gpu2.name, f"{gpu2.name} wins (index {idx2:.1f} vs {idx1:.1f})"
    else:
        winner, reasoning = "Tie", "Both GPUs show equal performance index"

    comparison = [
        {
            "name": gpu1.name,
            "vram_gb": float(gpu1.vram_gb),
            "core_count": gpu1.core_count,
            "core_clock_ghz": float(gpu1.core_clock_ghz),
            "memory_bandwidth_gbps": float(gpu1.memory_bandwidth_gbps),
            "ray_tracing_support": gpu1.ray_tracing_support,
            "performance_index": round(idx1, 2),
        },
        {
            "name": gpu2.name,
            "vram_gb": float(gpu2.vram_gb),
            "core_count": gpu2.core_count,
            "core_clock_ghz": float(gpu2.core_clock_ghz),
            "memory_bandwidth_gbps": float(gpu2.memory_bandwidth_gbps),
            "ray_tracing_support": gpu2.ray_tracing_support,
            "performance_index": round(idx2, 2),
        }
    ]

    return {
        "winner": winner,
        "reasoning": reasoning,
        "comparison": comparison
    }