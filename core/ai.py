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
Ты — помощник, который генерирует структурированные JSON-данные для визуализации барчартов на основе характеристик процессоров.

Я передаю тебе список процессоров с такими полями:
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

На основе этих данных сгенерируй JSON-массив, где каждый объект содержит:

- "name": название процессора
- "cores_threads": строка в формате "{core_count}c / {thread_count}t"
- "tdp": tdp_watts (в ваттах)
- "clock_speed": clock_speed_ghz (в ГГц)
- "l3_cache": cache_size_l3 (в МБ)
- "performance_score": core_count × clock_speed_ghz × ipc (округлить до 2 знаков)

Отсортируй по убыванию performance_score.

Верни ТОЛЬКО чистый JSON, без комментариев, пояснений и Markdown.
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
            raise ValueError("OPENROUTER_API_KEY не найден")

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek/deepseek-chat-v3-0324:free",
                "messages": [
                    {"role": "user", "content": cpu_promt + "\n\nДАННЫЕ:\n" + str(data)}
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
            print("Ошибка API:", response.status_code, response.text)
            return None

    except CPU.DoesNotExist as e:
        print(f"CPU не найден: {e}")
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
