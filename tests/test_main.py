import pytest

def calculate_modulo(numbers):
    result = []
    for i in range(0, len(numbers), 2):
        if i + 1 < len(numbers):
            result.append(numbers[i] % numbers[i + 1])
    return result

def test_calculate_modulo():
    numbers = [10, 2, 17, 5]
    expected_result = [0, 2]
    assert calculate_modulo(numbers) == expected_result

def test_calculate_modulo_with_odd_length_list():
    numbers = [10, 2, 17]
    expected_result = [0]
    assert calculate_modulo(numbers) == expected_result

def test_calculate_modulo_with_empty_list():
    numbers = []
    expected_result = []
    assert calculate_modulo(numbers) == expected_result

def test_calculate_modulo_with_single_element_list():
    numbers = [10]
    expected_result = []
    assert calculate_modulo(numbers) == expected_result
