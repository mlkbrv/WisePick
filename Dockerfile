# Используем официальный образ Python 3.12.11
FROM python:3.12.11-slim

# Переменные окружения для Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=WisePick.settings

# Устанавливаем системные зависимости для компиляции Python пакетов
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию
WORKDIR /code

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Удаляем компиляторы после установки зависимостей
RUN apt-get remove -y gcc g++ && apt-get autoremove -y && apt-get clean

# Копируем код приложения (включая .env если есть)
COPY . .

# Создаем непривилегированного пользователя для безопасности
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /code
USER appuser

# Открываем порт для Django
EXPOSE 8000

# Создаем скрипт инициализации
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Команда для запуска Django
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]