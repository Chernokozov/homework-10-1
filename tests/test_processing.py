"""Тесты для модуля processing."""

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state() -> None:
    """Тестирование фильтрации по статусу."""
    test_data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    executed_ops = filter_by_state(test_data)
    assert len(executed_ops) == 2
    assert all(op["state"] == "EXECUTED" for op in executed_ops)

    canceled_ops = filter_by_state(test_data, "CANCELED")
    assert len(canceled_ops) == 2
    assert all(op["state"] == "CANCELED" for op in canceled_ops)


def test_sort_by_date() -> None:
    """Тестирование сортировки по дате."""
    test_data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    sorted_desc = sort_by_date(test_data)
    assert sorted_desc[0]["id"] == 1  # Самая поздняя дата

    sorted_asc = sort_by_date(test_data, False)
    assert sorted_asc[0]["id"] == 2  # Самая ранняя дата
