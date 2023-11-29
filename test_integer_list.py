import pytest
from integer_list import IntegerList

@pytest.fixture
def integer_list():
    return IntegerList()

@pytest.mark.parametrize("nums, expected", [
    ([3], [3]),
    ([3, 5], [3, 5]),
    ([3, 5, 10], [3, 5, 10])
])
def test_add_integer(integer_list, nums, expected):
    for num in nums:
        integer_list.add_integer(num)
    assert integer_list.list == expected

@pytest.mark.parametrize("nums, num_to_remove, expected", [
    ([3, 5], 5, [3]),
    ([3, 5], 3, [5])
])
def test_remove_integer(integer_list, nums, num_to_remove, expected):
    for num in nums:
        integer_list.add_integer(num)
    integer_list.remove_integer(num_to_remove)
    assert integer_list.list == expected

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], 2),
    ([10, 20, 30], 20)
])
def test_get_average(integer_list, nums, expected):
    for num in nums:
        integer_list.add_integer(num)
    assert integer_list.get_average() == expected

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], 3),
    ([10, 20, 30], 30)
])
def test_get_max(integer_list, nums, expected):
    for num in nums:
        integer_list.add_integer(num)
    assert integer_list.get_max() == expected

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3], 1),
    ([10, 20, 30], 10)
])
def test_get_min(integer_list, nums, expected):
    for num in nums:
        integer_list.add_integer(num)
    assert integer_list.get_min() == expected
