"""Модуль виджета для обработки банковских операций."""

from datetime import datetime

from . import masks


def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер банковской карты или счета в зависимости от типа.

    Args:
        account_info: Строка с информацией о карте/счете

    Returns:
        Строка с замаскированным номером карты или счета
    """
    parts = account_info.split()

    if len(parts) < 2:
        raise ValueError("Неверный формат входных данных")

    account_type = " ".join(parts[:-1])
    number = parts[-1]

    if account_type.lower() == "счет":
        masked_number = masks.get_mask_account(number)
    else:
        masked_number = masks.get_mask_card_number(number)

    return f"{account_type} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

    Args:
        date_string: Дата в формате ISO

    Returns:
        Дата в формате ДД.ММ.ГГГГ
    """
    try:
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError as e:
        raise ValueError(f"Неверный формат даты: {date_string}") from e
