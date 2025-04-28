FROM python:3.12-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Настройка Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установка зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копирование проекта
COPY . .

# Команда запуска
CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:8082", "task_manager.wsgi"]