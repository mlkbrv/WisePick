import json
import os
import sys
import django
import requests
from dotenv import load_dotenv
from core.models import CPU, GPU, RAM, Needs, Phone, BrandsCoefficients

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WisePick.settings')
django.setup()

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# =====GETAPIKEY=====
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found")

# =====Promts=========
cpu_prompt = """
You are an assistant that generates structured JSON data for bar chart visualization based on processor characteristics.

I provide you with a list of processors with the following fields:
- name
- clock_speed_ghz
- core_count
- thread_count
- cache_size_l1
- cache_size_l2
- cache_size_l3
- tdp_watts
- architecture_generation
- ipc

Based on this data, generate a JSON array where each object contains:

- "name": processor name
- "cores_threads": string in format "{core_count}c / {thread_count}t"
- "tdp": tdp_watts (in watts)
- "clock_speed": clock_speed_ghz (in GHz)
- "l3_cache": cache_size_l3 (in MB)
- "performance_score": core_count × clock_speed_ghz × ipc (rounded to 2 decimal places)

Sort by performance_score in descending order.

Return ONLY clean JSON, without comments, explanations, or Markdown.
"""
gpu_prompt = """
You are an assistant that generates structured JSON data for bar chart visualization based on GPU characteristics.

I provide you with a list of GPUs with the following fields:
- name
- vram_gb
- core_count
- core_clock_ghz
- memory_bandwidth_gbps
- architecture
- ray_tracing_support
- release_year

Based on this data, generate a JSON array where each object contains:

- "name": GPU name
- "vram": vram_gb (in GB)
- "core_clock": core_clock_ghz (in GHz)
- "memory_bandwidth": memory_bandwidth_gbps (in GB/s)
- "ray_tracing": "Yes" if ray_tracing_support is True, otherwise "No"
- "performance_score": core_count × core_clock_ghz × memory_bandwidth_gbps (rounded to 2 decimal places)

Sort by performance_score in descending order.

Return ONLY clean JSON, without comments, explanations, or Markdown.
"""
ram_prompt = """
You are an assistant that generates structured JSON data for bar chart visualization based on RAM characteristics.

I provide you with a list of RAM modules with the following fields:
- name
- size_gb
- speed_mhz
- type

Based on this data, generate a JSON array where each object contains:

- "name": RAM name
- "size": size_gb (in GB)
- "speed": speed_mhz (in MHz)
- "type": RAM type (e.g., DDR4, DDR5)
- "performance_score": size_gb × speed_mhz (rounded to 2 decimal places)

Sort by performance_score in descending order.

Return ONLY clean JSON, without comments, explanations, or Markdown.
"""

# =====Tools=====
def clean_json_response(text):
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()


def get_gpu_comparison_json(gpu1_name: str, gpu2_name: str):
    try:
        gpu1 = GPU.objects.get(name=gpu1_name)
        gpu2 = GPU.objects.get(name=gpu2_name)

        gpu1_score = gpu1.core_count * gpu1.core_clock_ghz * gpu1.memory_bandwidth_gbps
        gpu2_score = gpu2.core_count * gpu2.core_clock_ghz * gpu2.memory_bandwidth_gbps

        if gpu1_score > gpu2_score:
            winner = gpu1.name
            reasoning = f"{gpu1.name} wins with higher performance score ({gpu1_score:.2f} vs {gpu2_score:.2f})"
        elif gpu2_score > gpu1_score:
            winner = gpu2.name
            reasoning = f"{gpu2.name} wins with higher performance score ({gpu2_score:.2f} vs {gpu1_score:.2f})"
        else:
            winner = "Tie"
            reasoning = "Both GPUs have similar performance scores"

        data = [
            {
                "name": gpu1.name,
                "vram_gb": float(gpu1.vram_gb),
                "core_count": gpu1.core_count,
                "core_clock_ghz": float(gpu1.core_clock_ghz),
                "memory_bandwidth_gbps": float(gpu1.memory_bandwidth_gbps),
                "ray_tracing_support": gpu1.ray_tracing_support,
            },
            {
                "name": gpu2.name,
                "vram_gb": float(gpu2.vram_gb),
                "core_count": gpu2.core_count,
                "core_clock_ghz": float(gpu2.core_clock_ghz),
                "memory_bandwidth_gbps": float(gpu2.memory_bandwidth_gbps),
                "ray_tracing_support": gpu2.ray_tracing_support,
            }
        ]

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek/deepseek-chat-v3-0324:free",
                "messages": [
                    {"role": "user", "content": gpu_prompt + "\n\nDATA:\n" + str(data)}
                ],
                "temperature": 0.1
            }
        )
        if response.status_code == 200:
            result = response.json()
            print(f"GPU API Response: {result}")

            if 'choices' in result and len(result['choices']) > 0:
                content = result['choices'][0]['message']['content']
                cleaned = clean_json_response(content)
                return json.loads(cleaned)
            elif 'error' in result:
                print(f"API returned error: {result['error']}")
                return None
            else:
                print(f"Unexpected API response format: {result}")
                return {
                    "winner": winner,
                    "reasoning": reasoning,
                    "comparison": data
                }
        else:
            print("API Error:", response.status_code, response.text)
            return {
                "winner": winner,
                "reasoning": reasoning,
                "comparison": data
            }

    except GPU.DoesNotExist as e:
        print(f"GPU not found: {e}")
        return None


def get_cpu_comparison_json(cpu1_name: str, cpu2_name: str):
    try:
        cpu1 = CPU.objects.get(name=cpu1_name)
        cpu2 = CPU.objects.get(name=cpu2_name)

        cpu1_score = cpu1.core_count * cpu1.clock_speed_ghz * cpu1.ipc
        cpu2_score = cpu2.core_count * cpu2.clock_speed_ghz * cpu2.ipc

        if cpu1_score > cpu2_score:
            winner = cpu1.name
            reasoning = f"{cpu1.name} wins with higher performance score ({cpu1_score:.2f} vs {cpu2_score:.2f})"
        elif cpu2_score > cpu1_score:
            winner = cpu2.name
            reasoning = f"{cpu2.name} wins with higher performance score ({cpu2_score:.2f} vs {cpu1_score:.2f})"
        else:
            winner = "Tie"
            reasoning = "Both CPUs have similar performance scores"

        data = [
            {
                "name": cpu1.name,
                "clock_speed_ghz": float(cpu1.clock_speed_ghz),
                "core_count": cpu1.core_count,
                "thread_count": cpu1.thread_count,
                "tdp_watts": cpu1.tdp_watts,
                "ipc": float(cpu1.ipc),
            },
            {
                "name": cpu2.name,
                "clock_speed_ghz": float(cpu2.clock_speed_ghz),
                "core_count": cpu2.core_count,
                "thread_count": cpu2.thread_count,
                "tdp_watts": cpu2.tdp_watts,
                "ipc": float(cpu2.ipc),
            }
        ]

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek/deepseek-chat-v3-0324:free",
                "messages": [
                    {"role": "user", "content": cpu_prompt + "\n\nDATA:\n" + str(data)}
                ],
                "temperature": 0.1
            }
        )

        if response.status_code == 200:
            result = response.json()
            print(f"CPU API Response: {result}")  # Debug log

            if 'choices' in result and len(result['choices']) > 0:
                content = result['choices'][0]['message']['content']
                cleaned = clean_json_response(content)
                return json.loads(cleaned)
            elif 'error' in result:
                print(f"API returned error: {result['error']}")
                return {
                    "winner": winner,
                    "reasoning": reasoning,
                    "comparison": data
                }
            else:
                print(f"Unexpected API response format: {result}")
                return {
                    "winner": winner,
                    "reasoning": reasoning,
                    "comparison": data
                }
        else:
            print("API Error:", response.status_code, response.text)
            return {
                "winner": winner,
                "reasoning": reasoning,
                "comparison": data
            }

    except CPU.DoesNotExist as e:
        print(f"CPU not found: {e}")
        return None


def get_ram_comparison_json(ram1_name: str, ram2_name: str):
    try:
        ram1 = RAM.objects.get(name=ram1_name)
        ram2 = RAM.objects.get(name=ram2_name)

        ram1_score = ram1.size_gb * ram1.speed_mhz
        ram2_score = ram2.size_gb * ram2.speed_mhz

        if ram1_score > ram2_score:
            winner = ram1.name
            reasoning = f"{ram1.name} wins with higher performance score ({ram1_score:.2f} vs {ram2_score:.2f})"
        elif ram2_score > ram1_score:
            winner = ram2.name
            reasoning = f"{ram2.name} wins with higher performance score ({ram2_score:.2f} vs {ram1_score:.2f})"
        else:
            winner = "Tie"
            reasoning = "Both RAM modules have similar performance scores"

        data = [
            {
                "name": ram1.name,
                "size": ram1.size_gb,
                "speed": ram1.speed_mhz,
                "type": ram1.type,
                "performance_score": round(ram1.size_gb * ram1.speed_mhz, 2)
            },
            {
                "name": ram2.name,
                "size": ram2.size_gb,
                "speed": ram2.speed_mhz,
                "type": ram2.type,
                "performance_score": round(ram2.size_gb * ram2.speed_mhz, 2)
            }
        ]

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek/deepseek-chat-v3-0324:free",
                "messages": [
                    {"role": "user", "content": ram_prompt + "\n\nDATA:\n" + str(data)}
                ],
                "temperature": 0.1
            }
        )

        if response.status_code == 200:
            result = response.json()
            print(f"RAM API Response: {result}")  # Debug log

            if 'choices' in result and len(result['choices']) > 0:
                content = result['choices'][0]['message']['content']
                cleaned = clean_json_response(content)
                return json.loads(cleaned)
            elif 'error' in result:
                print(f"API returned error: {result['error']}")
                return {
                    "winner": winner,
                    "reasoning": reasoning,
                    "comparison": data
                }
            else:
                print(f"Unexpected API response format: {result}")
                return {
                    "winner": winner,
                    "reasoning": reasoning,
                    "comparison": data
                }
        else:
            print("API Error:", response.status_code, response.text)
            return {
                "winner": winner,
                "reasoning": reasoning,
                "comparison": data
            }

    except RAM.DoesNotExist as e:
        print(f"RAM not found: {e}")
        return None


def get_pc_comparison_json(pc1_components: dict, pc2_components: dict, need_description: str = None):
    try:
        cpu1 = CPU.objects.get(name=pc1_components.get('cpu_name'))
        gpu1 = GPU.objects.get(name=pc1_components.get('gpu_name'))
        ram1 = RAM.objects.get(name=pc1_components.get('ram_name'))

        cpu2 = CPU.objects.get(name=pc2_components.get('cpu_name'))
        gpu2 = GPU.objects.get(name=pc2_components.get('gpu_name'))
        ram2 = RAM.objects.get(name=pc2_components.get('ram_name'))

        pc1_data = {
            "name": f"PC1 ({cpu1.name} + {gpu1.name} + {ram1.name})",
            "cpu": {
                "name": cpu1.name,
                "clock_speed_ghz": float(cpu1.clock_speed_ghz),
                "core_count": cpu1.core_count,
                "thread_count": cpu1.thread_count,
                "tdp_watts": cpu1.tdp_watts,
                "ipc": float(cpu1.ipc),
                "performance_score": round(cpu1.core_count * cpu1.clock_speed_ghz * cpu1.ipc, 2)
            },
            "gpu": {
                "name": gpu1.name,
                "vram_gb": float(gpu1.vram_gb),
                "core_count": gpu1.core_count,
                "core_clock_ghz": float(gpu1.core_clock_ghz),
                "memory_bandwidth_gbps": float(gpu1.memory_bandwidth_gbps),
                "ray_tracing_support": gpu1.ray_tracing_support,
                "performance_score": round(gpu1.core_count * gpu1.core_clock_ghz * gpu1.memory_bandwidth_gbps, 2)
            },
            "ram": {
                "name": ram1.name,
                "size_gb": ram1.size_gb,
                "speed_mhz": ram1.speed_mhz,
                "type": ram1.type,
                "performance_score": round(ram1.size_gb * ram1.speed_mhz, 2)
            }
        }

        pc2_data = {
            "name": f"PC2 ({cpu2.name} + {gpu2.name} + {ram2.name})",
            "cpu": {
                "name": cpu2.name,
                "clock_speed_ghz": float(cpu2.clock_speed_ghz),
                "core_count": cpu2.core_count,
                "thread_count": cpu2.thread_count,
                "tdp_watts": cpu2.tdp_watts,
                "ipc": float(cpu2.ipc),
                "performance_score": round(cpu2.core_count * cpu2.clock_speed_ghz * cpu2.ipc, 2)
            },
            "gpu": {
                "name": gpu2.name,
                "vram_gb": float(gpu2.vram_gb),
                "core_count": gpu2.core_count,
                "core_clock_ghz": float(gpu2.core_clock_ghz),
                "memory_bandwidth_gbps": float(gpu2.memory_bandwidth_gbps),
                "ray_tracing_support": gpu2.ray_tracing_support,
                "performance_score": round(gpu2.core_count * gpu2.core_clock_ghz * gpu2.memory_bandwidth_gbps, 2)
            },
            "ram": {
                "name": ram2.name,
                "size_gb": ram2.size_gb,
                "speed_mhz": ram2.speed_mhz,
                "type": ram2.type,
                "performance_score": round(ram2.size_gb * ram2.speed_mhz, 2)
            }
        }

        comparison_prompt = f"""
You are an assistant that compares two PC configurations based on user needs and generates structured JSON data.

I provide you with two PC configurations and a user need description. Each PC has CPU, GPU, and RAM components with their specifications.

User Need: {need_description or "General purpose computing"}

PC Configurations:
PC1: {pc1_data['name']}
- CPU: {pc1_data['cpu']['name']} ({pc1_data['cpu']['core_count']}c/{pc1_data['cpu']['thread_count']}t, {pc1_data['cpu']['clock_speed_ghz']}GHz)
- GPU: {pc1_data['gpu']['name']} ({pc1_data['gpu']['vram_gb']}GB VRAM)
- RAM: {pc1_data['ram']['name']} ({pc1_data['ram']['size_gb']}GB {pc1_data['ram']['type']}, {pc1_data['ram']['speed_mhz']}MHz)

PC2: {pc2_data['name']}
- CPU: {pc2_data['cpu']['name']} ({pc2_data['cpu']['core_count']}c/{pc2_data['cpu']['thread_count']}t, {pc2_data['cpu']['clock_speed_ghz']}GHz)
- GPU: {pc2_data['gpu']['name']} ({pc2_data['gpu']['vram_gb']}GB VRAM)
- RAM: {pc2_data['ram']['name']} ({pc2_data['ram']['size_gb']}GB {pc2_data['ram']['type']}, {pc2_data['ram']['speed_mhz']}MHz)

Based on the user need and component specifications, generate a JSON object with the following structure:

{{
    "comparison": [
        {{
            "pc_name": "PC1",
            "overall_score": <score from 0-100>,
            "cpu_score": <score from 0-100>,
            "gpu_score": <score from 0-100>,
            "ram_score": <score from 0-100>,
            "recommendation": "<brief recommendation based on need>",
            "strengths": ["<strength1>", "<strength2>", "<strength3>"],
            "weaknesses": ["<weakness1>", "<weakness2>"]
        }},
        {{
            "pc_name": "PC2",
            "overall_score": <score from 0-100>,
            "cpu_score": <score from 0-100>,
            "gpu_score": <score from 0-100>,
            "ram_score": <score from 0-100>,
            "recommendation": "<brief recommendation based on need>",
            "strengths": ["<strength1>", "<strength2>", "<strength3>"],
            "weaknesses": ["<weakness1>", "<weakness2>"]
        }}
    ],
    "winner": "<PC1 or PC2>",
    "reasoning": "<detailed explanation of why this PC is better for the given need>"
}}

Return ONLY clean JSON, without comments, explanations, or Markdown.
"""

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek/deepseek-chat-v3-0324:free",
                "messages": [
                    {"role": "user", "content": comparison_prompt}
                ],
                "temperature": 0.1
            }
        )

        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            cleaned = clean_json_response(content)
            return json.loads(cleaned)
        else:
            print("API Error:", response.status_code, response.text)
            return None

    except (CPU.DoesNotExist, GPU.DoesNotExist, RAM.DoesNotExist) as e:
        print(f"Component not found: {e}")
        return None
    except Exception as e:
        print(f"Error comparing PCs: {e}")
        return None


def get_phone_comparison_json(phone1_name: str, phone2_name: str, need_description: str = None):
    try:
        phone1 = Phone.objects.get(name=phone1_name)
        phone2 = Phone.objects.get(name=phone2_name)

        brand_coeffs = dict(BrandsCoefficients.objects.values_list('name', 'coefficient'))

        phone1_data = {
            "name": phone1.name,
            "brand": phone1.brand,
            "ram_size": phone1.ram_size,
            "memory_size": phone1.memory_size,
            "processor": phone1.processor,
            "camera_mp": phone1.camera_mp,
            "battery": phone1.battery,
            "year": phone1.year,
            "brand_coefficient": brand_coeffs.get(phone1.brand, 1.0)
        }

        phone2_data = {
            "name": phone2.name,
            "brand": phone2.brand,
            "ram_size": phone2.ram_size,
            "memory_size": phone2.memory_size,
            "processor": phone2.processor,
            "camera_mp": phone2.camera_mp,
            "battery": phone2.battery,
            "year": phone2.year,
            "brand_coefficient": brand_coeffs.get(phone2.brand, 1.0)
        }

        comparison_prompt = f"""
You are an assistant that compares two smartphones based on user needs and component specifications.

User Need: {need_description or "General purpose smartphone usage"}

Each phone has brand-based coefficients that influence its overall performance, reliability, and optimization quality.

Phone 1:
{phone1_data}

Phone 2:
{phone2_data}

Brand Coefficients:
{brand_coeffs}

Generate a JSON object with the following structure:
{{
    "comparison": [
        {{
            "phone_name": "Phone1",
            "overall_score": <score from 0-100>,
            "performance_score": <score from 0-100>,
            "camera_score": <score from 0-100>,
            "battery_score": <score from 0-100>,
            "recommendation": "<brief recommendation based on user need>",
            "strengths": ["<strength1>", "<strength2>", "<strength3>"],
            "weaknesses": ["<weakness1>", "<weakness2>"]
        }},
        {{
            "phone_name": "Phone2",
            "overall_score": <score from 0-100>,
            "performance_score": <score from 0-100>,
            "camera_score": <score from 0-100>,
            "battery_score": <score from 0-100>,
            "recommendation": "<brief recommendation based on user need>",
            "strengths": ["<strength1>", "<strength2>", "<strength3>"],
            "weaknesses": ["<weakness1>", "<weakness2>"]
        }}
    ],
    "winner": "<Phone1 or Phone2>",
    "reasoning": "<detailed explanation of which phone better fits the described need>"
}}

Return ONLY pure JSON (no markdown or text).
"""

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek/deepseek-chat-v3-0324:free",
                "messages": [
                    {"role": "user", "content": comparison_prompt}
                ],
                "temperature": 0.1
            }
        )

        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            cleaned = clean_json_response(content)
            return json.loads(cleaned)
        else:
            print("API Error:", response.status_code, response.text)
            return None

    except Phone.DoesNotExist as e:
        print(f"Phone not found: {e}")
        return None
    except Exception as e:
        print(f"Error comparing phones: {e}")
        return None
