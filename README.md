# notebook

## Описание проекта
notebook - api-сервис разработанный с использованием Fast API и Redis. Даёт удобный способ временного чтения, создания, перезаписи телефонов и адрессов организации в виде ключ-значение.

## Технологии
- Python 3.13 (FastAPI 0.115.12)
- Docker
- Redis

## Установка и запуск

1. Клонируйте репозиторий и зайдите в него:
```bash
git clone 'https://github.com/Den-Krutov/notebook.git'
cd notebook
```

2. Создайте и поднимите контейнеры:
```bash
docker-compose up -d --build
```

## Эндпоинты
- `/api/v1/organizations/check_data?phone=xxx` - поиск организации по телефону
- `/api/v1/organizations/write_data` - создание или перезапись организации

## Авторы
Даниил Федин (GitHub https://github.com/Den-Krutov)
