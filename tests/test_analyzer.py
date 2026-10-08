import pytest

from backend.services.analyzer import Status, evaluate_result

def test_value_in_range():
    assert evaluate_result(5.0, 3.9, 5.5) == Status.NORMAL


def test_value_below_range():
    assert evaluate_result(3.0, 3.9, 5.5) == Status.LOW


def test_value_above_range():
    assert evaluate_result(6.1, 3.9, 5.5) == Status.HIGH


def test_boundary_values_are_normal():
    assert evaluate_result(3.9, 3.9, 5.5) == Status.NORMAL
    assert evaluate_result(5.5, 3.9, 5.5) == Status.NORMAL


def test_missing_reference():
    assert evaluate_result(5.0, None, 5.5) == Status.UNKNOWN


def test_invalid_reference_raises():
    with pytest.raises(ValueError):
        evaluate_result(5.0, 5.5, 3.9)