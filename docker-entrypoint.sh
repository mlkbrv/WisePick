#!/bin/bash

# Ожидаем, пока Redis станет доступным
echo "Waiting for Redis to be available..."
while ! redis-cli -h redis ping > /dev/null 2>&1; do
    echo "Redis is unavailable - sleeping"
    sleep 1
done
echo "Redis is up - continuing"

# Выполняем миграции
echo "Running database migrations..."
python manage.py migrate --noinput

# Создаем суперпользователя, если его нет
echo "Creating superuser if not exists..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
"

# Заполняем базу данных тестовыми данными
echo "Populating database with sample data..."
python populate_data.py

# Собираем статические файлы
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Запускаем команду, переданную в CMD
echo "Starting application..."
exec "$@"
