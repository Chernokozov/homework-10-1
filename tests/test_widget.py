"""Тесты для модуля widget."""

from src.widget import get_date, mask_account_card


def test_mask_account_card() -> None:
    """Тестирование маскировки карт и счетов."""
    test_cases = [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ]

    for input_data, expected in test_cases:
        result = mask_account_card(input_data)
        assert result == expected


def test_get_date() -> None:
    """Тестирование форматирования дат."""
    test_cases = [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-31T23:59:59.999999", "31.12.2023"),
    ]

    for input_data, expected in test_cases:
        result = get_date(input_data)
        assert result == expected
