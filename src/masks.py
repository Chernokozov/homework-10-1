"""Модуль для маскировки номеров карт и счетов."""


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, оставляя видимыми первые 6 и последние 4 цифры.

    Args:
        card_number: Номер карты для маскировки

    Returns:
        Замаскированный номер карты в формате XXXX XX** **** XXXX
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя видимыми только последние 4 цифры.

    Args:
        account_number: Номер счета для маскировки

    Returns:
        Замаскированный номер счета в формате **XXXX
    """
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    return f"**{account_number[-4:]}"
