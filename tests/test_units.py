import pytest
from src.units import to_sqwah, from_sqwah, to_rai_decimal


def test_one_rai():
    assert to_sqwah(1, 0, 0) == 400


def test_mixed():
    assert to_sqwah(2, 1, 50) == 950


def test_round_trip():
    assert from_sqwah(950) == (2, 1, 50)


def test_zero():
    assert to_sqwah(0, 0, 0) == 0


def test_rai_decimal():
    assert to_rai_decimal(1, 2, 0) == 1.5


def test_negative():
    with pytest.raises(ValueError):
        to_sqwah(-1, 0, 0)
