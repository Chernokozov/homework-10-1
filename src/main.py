"""Основной модуль для демонстрации работы виджета."""

from .widget import mask_account_card, get_date
from .processing import filter_by_state, sort_by_date

def main() -> None:
    """Демонстрация работы всех функций виджета."""
    print("=== Bank Operations Widget Demo ===\n")

    # Демонстрация маскировки
    print("1. Маскировка карт и счетов:")
    test_cards = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "Visa Platinum 7000792289606361",
    ]

    for card in test_cards:
        masked = mask_account_card(card)
        print(f"   {card} -> {masked}")

    # Демонстрация форматирования дат
    print("\n2. Форматирование дат:")
    test_dates = [
        "2024-03-11T02:26:18.671407",
        "2023-12-31T23:59:59.999999",
    ]

    for date_str in test_dates:
        formatted = get_date(date_str)
        print(f"   {date_str} -> {formatted}")

    # Демонстрация обработки операций
    print("\n3. Обработка операций:")
    operations = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    executed = filter_by_state(operations)
    print(f"   Выполненные операции: {len(executed)}")

    sorted_ops = sort_by_date(operations)
    print(f"   Отсортированные операции: {len(sorted_ops)}")


if __name__ == "__main__":
    main()