import matplotlib.pyplot as plt
import json
import os
import sys
import django
import requests
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WisePick.settings')
django.setup()

from core.models import CPU

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

cpu_promt = """
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

def get_cpu_comparison_json(cpu1_name: str, cpu2_name: str):
    try:
        cpu1 = CPU.objects.get(name=cpu1_name)
        cpu2 = CPU.objects.get(name=cpu2_name)

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

        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found")

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek/deepseek-chat-v3-0324:free",
                "messages": [
                    {"role": "user", "content": cpu_promt + "\n\nDATA:\n" + str(data)}
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

    except CPU.DoesNotExist as e:
        print(f"CPU not found: {e}")
        return None

def clean_json_response(text):
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()
