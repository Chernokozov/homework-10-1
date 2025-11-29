# Bank Operations Widget

Виджет для обработки и отображения банковских операций клиента.

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/bank-operations-widget.git
cd bank-operations-widget

```
2. Установите зависимости с помощью Poetry:
```bash

poetry install

```

3. Активируйте виртуальное окружение:
```bash

poetry shell
```
4. Запустите демо:
```bash

poetry run bank-widget

```
## Или напрямую:
```bash

python -m src.main

```

## Тестирование
```bash

# Запуск всех тестов
poetry run pytest

# Запуск с подробным выводом
poetry run pytest -v

# Запуск конкретного тестового файла
poetry run pytest tests/test_widget.py
Проверка кодстайла
```
```bash
# Flake8
poetry run flake8 src/ tests/

# MyPy
poetry run mypy src/ tests/

# isort
poetry run isort src/ tests/ --check-only

# black
poetry run black src/ tests/ --check
```
## Использование в коде
```python
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date

# Маскировка
masked_card = mask_account_card("Visa Platinum 7000792289606361")

# Форматирование даты
formatted_date = get_date("2024-03-11T02:26:18.671407")

# Обработка операций
executed_ops = filter_by_state(operations)
sorted_ops = sort_by_date(operations)
```

## Разработка
Проект использует:

Poetry для управления зависимостями

Pytest для тестирования

Flake8, MyPy, isort, black для контроля качества кода

GitFlow для workflow




## 9. Команды для работы с проектом

```bash

# Активация окружения
poetry shell

# Добавление новых зависимостей
poetry add package_name

# Добавление dev зависимостей
poetry add --group dev package_name

# Запуск линтеров
poetry run flake8 src/
poetry run mypy src/
poetry run isort src/
poetry run black src/

# Запуск тестов
poetry run pytest

# Сборка пакета
poetry build
```