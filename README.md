# testovoe_zadaniye
# Тестовое задание: API для управления задачами (Django)

Реализация REST API для управления задачами (tasks) с использованием Django и Django REST Framework.

SECRET_KEY=django-insecure-^7(sd*(nu0s_f4hocl(rhd^7y*8t4+npxq26o5e051sc4@&9k3

## Описание задачи

API для создания, чтения, обновления и удаления задач с полями:

- `id`: int
- `title`: str
- `description`: str
- `is_completed`: bool (по умолчанию `False`)
- `created_at`: datetime
- `updated_at`: datetime

---

## Эндпоинты

| Метод  | URL             | Описание                  |
|--------|-----------------|---------------------------|
| POST   | `/tasks/`       | Создать новую задачу      |
| GET    | `/tasks/`       | Получить список всех задач|
| GET    | `/tasks/{id}/`  | Получить задачу по ID     |
| PUT    | `/tasks/{id}/`  | Обновить задачу по ID     |
| DELETE | `/tasks/{id}/`  | Удалить задачу по ID      |

---

## Технологии

- Язык: Python 3.10+
- Фреймворк: Django 5.2, Django REST Framework 3.16
- База данных: PostgreSQL
- Документация API: drf-yasg (Swagger/OpenAPI)
- Формат ответа: JSON
- Docker и Docker Compose для контейнеризации

### 1. Клонировать репозиторий

```bash
git clone github.com:daisy919231/testovoe_zadaniye.git
cd testovoe_zadaniye

## Установка и запуск
Основные команды
Команда	Описание
docker compose up --build	Сборка и запуск контейнеров
docker compose exec web python manage.py migrate	Применение миграций базы
docker compose exec web python manage.py test	Запуск тестов


**Комментарии по коду**
Используется Django ORM и миграции для работы с базой

REST API построено с использованием Django REST Framework

Документация API реализована через drf-yasg (Swagger/OpenAPI)

Контейнеризация с помощью Docker и Docker Compose упрощает развёртывание

Тесты покрывают основные сценарии CRUD


**Открыть API и документацию**
API доступен по адресу: http://localhost:8000/tasks/

Swagger UI документация: http://localhost:8000/swagger/

Контакты
Если возникнут вопросы — пишите: shahzodaakhmedova91@gmail.com


