# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем зависимости для Node.js и npm
RUN apt-get update && apt-get install -y nodejs npm

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Устанавливаем зависимости Node.js и компилируем Tailwind CSS
RUN npm install
RUN npx tailwindcss build src/styles.css -o static/css/tailwind.css

# Собираем статику
RUN python manage.py collectstatic --noinput

# Указываем команду для запуска сервера
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "your_project_name.wsgi:application"]
