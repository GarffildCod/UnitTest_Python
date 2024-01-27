"""Модуль тестов"""
from main import ListComparator

comparator = ListComparator()


def test_compare_lists_first_bigger_second():
    """
    Проверяет, что при сравнении списков первый список имеет большее среднее значение.
    """
    list1 = [6, 7, 8, 9, 10]
    list2 = [1, 2, 3, 4, 5]
    assert comparator.compare_lists(list1, list2) == "Первый список имеет большее среднее значение"


def test_compare_lists_second_bigger_first():
    """
    Проверяет, что при сравнении списков второй список имеет большее среднее значение.
    """
    list3 = [1, 2, 3, 4, 5]
    list4 = [6, 7, 8, 9, 10]
    assert comparator.compare_lists(list3, list4) == "Второй список имеет большее среднее значение"


def test_compare_lists_first_equal_second():
    """
    Проверяет, что при сравнении списков их средние значения равны.
    """
    list5 = [1, 2, 3, 4, 5]
    list6 = [1, 2, 3, 4, 5]
    assert comparator.compare_lists(list5, list6) == "Средние значения равны"


def test_calculate_average():
    """
    Проверяет корректность расчета среднего значения списка.
    """
    list7 = [10, 20, 30, 40, 50]
    assert comparator.calculate_average(list7) == 30.0