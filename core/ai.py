# core/plot_cpu.py

import matplotlib.pyplot as plt
import json
import os
import sys
import django
import requests
from dotenv import load_dotenv

# === Настройка Django ===
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WisePick.settings')
django.setup()

from core.models import CPU

# === Загрузка .env ===
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# === Промт для ИИ (БЕЗ ГОДА!) ===
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
            return result['choices'][0]['message']['content']
        else:
            print("Ошибка API:", response.status_code, response.text)
            return None

    except CPU.DoesNotExist as e:
        print(f"CPU не найден: {e}")
        return None


# === Очистка Markdown-обёртки ===
def clean_json_response(text):
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()


# === Построение барчарта (горизонтальный, как на изображении) ===
def plot_cpu_barchart(json_data):
    try:
        cpus = json.loads(json_data)
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return

    # Данные
    names = [cpu['name'] for cpu in cpus]
    cores_threads = [cpu['cores_threads'] for cpu in cpus]
    tdp = [cpu['tdp'] for cpu in cpus]
    performance = [cpu['performance_score'] for cpu in cpus]

    # Процентное увеличение (относительно предыдущего)
    percentages = [None]  # Первый — нет сравнения
    for i in range(1, len(performance)):
        change = ((performance[i] - performance[i-1]) / performance[i-1]) * 100
        percentages.append(change)

    # === Настройка графика ===
    fig, ax = plt.subplots(figsize=(14, 6))

    # Горизонтальные столбцы
    bars = ax.barh(names, performance, color='#27ae60', edgecolor='none', height=0.6)

    # Убираем рамки
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_linewidth(0.5)

    # Подписи справа от баров
    for i, (bar, perf, pct) in enumerate(zip(bars, performance, percentages)):
        ax.text(perf + max(performance)*0.01, bar.get_y() + bar.get_height()/2,
                f'{perf:.2f}', va='center', ha='left', fontsize=11, fontweight='bold')

        # Процентное изменение (если есть)
        if pct is not None:
            ax.text(perf + max(performance)*0.01, bar.get_y() + bar.get_height()/2 + 0.15,
                    f'+{pct:.1f}%', va='center', ha='left', fontsize=9, color='purple')

    # Левая сторона: название и характеристики
    for i, (name, ct, t) in enumerate(zip(names, cores_threads, tdp)):
        ax.text(-max(performance)*0.05, i + 0.2, name, ha='left', va='center', fontsize=11, fontweight='bold')
        ax.text(-max(performance)*0.05, i - 0.0, f'{ct}, {t}W', ha='left', va='center', fontsize=9, color='gray')

    # Ось X
    ax.set_xlim(0, max(performance) * 1.2)
    ax.set_xticks([])
    ax.set_yticks([])

    # Заголовок
    ax.set_title('Сравнение производительности процессоров', fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.show()


# === Запуск ===
if __name__ == "__main__":
    result = get_cpu_comparison_json("Intel Core i9-12900K", "AMD Ryzen 7 7700X")
    if result:
        cleaned = clean_json_response(result)
        plot_cpu_barchart(cleaned)
    else:
        print("Не удалось получить данные от ИИ.")