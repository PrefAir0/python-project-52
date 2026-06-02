### Hexlet tests and linter status:
[![Actions Status](https://github.com/PrefAir0/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/PrefAir0/python-project-52/actions)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=PrefAir0_python-project-52&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=PrefAir0_python-project-52)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=PrefAir0_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=PrefAir0_python-project-52)

# Менеджер задач (Task Manager)

### Описание
**Менеджер задач** — это веб-приложение для управления проектами, постановки задач, назначения исполнителей и отслеживания статусов.

Основные возможности:
* **Пользователи:** Регистрация, аутентификация и управление профилями
* **Статусы:** Создание и гибкая настройка жизненного цикла задачи
* **Задачи:** Постановка задач с указанием описания, исполнителя и статуса
* **Метки:** Добавление тегов (меток) к задачам для удобной группировки
* **Фильтрация:** Продвинутый поиск задач по автору, исполнителю, статусу и меткам

---

### Стек технологий
* **Бэкенд:** Django
* **База данных:** PostgreSQL / SQLite (Локально)
* **Менеджер зависимостей:** Poetry

---

### Установка и запуск проекта
* Установи зависимости с помощью uv sync
* В `.env` добавьте секретный ключь django: `SECRET_KEY=your_secret_key`
* Выполните миграцию базы данных: `poetry run python manage.py migrate`
* Зпустите сервер: `poetry run python manage.py runserver`
