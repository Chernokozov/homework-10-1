"""Модуль для обработки банковских операций."""

from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(
    operations: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует операции по статусу выполнения.

    Args:
        operations: Список операций
        state: Статус для фильтрации

    Returns:
        Отфильтрованный список операций
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
    operations: List[Dict[str, Any]], descending: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует операции по дате.

    Args:
        operations: Список операций
        descending: Порядок сортировки

    Returns:
        Отсортированный список операций
    """

    def get_date_key(operation: Dict[str, Any]) -> datetime:
        date_str = operation.get("date", "")
        return datetime.fromisoformat(date_str) if date_str else datetime.min

    return sorted(operations, key=get_date_key, reverse=descending)
