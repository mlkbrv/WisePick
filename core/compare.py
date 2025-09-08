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

