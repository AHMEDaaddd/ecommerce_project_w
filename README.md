# 🛍️ E-commerce Project — Задание 14.2 (SkyPro)

## 📌 Описание

Проект демонстрирует применение объектно-ориентированного программирования (ООП) в Python:

- Инкапсуляция с приватными атрибутами (`__price`)
- Использование геттеров и сеттеров через `@property`
- Метод `add_product()` с проверкой на тип (`isinstance`)
- Использование `@classmethod` для создания объектов
- Покрытие проекта тестами с помощью `pytest`

## 📦 Структура

```
ecommerce_project/
├── src/
│   └── models.py          # Классы Product и Category
├── tests/
│   └── test_models.py     # Unit-тесты
├── pyproject.toml         # Конфигурация Poetry
└── README.md              # Описание проекта
```

## 🚀 Быстрый старт

### Установка зависимостей:

```bash
poetry install
```

### Проверка кода:

```bash
# Проверка типов
poetry run mypy src tests

# Проверка стиля
poetry run flake8 src tests
poetry run pydocstyle src

# Тесты с покрытием
poetry run pytest --cov=src --cov-report=term-missing
```

## ✅ Критерии задания 14.2

- [x] Атрибут `__price` приватный
- [x] Реализован `@property` геттер `price`
- [x] Реализован сеттер с проверкой `value > 0`
- [x] Метод `add_product()` использует `isinstance`
- [x] Написаны и проходят unit-тесты

## 👨‍💻 Автор

# Версия проекта с доработанным геттером и сеттером — для задачи 14.2