import pytest
from src.core.common.validates import (
    _validate_input,
    _generate_first_digit,
    _generate_second_digit,
    validate_cpf,
)


def test_validate_input():
    assert _validate_input("123.456.789-09")
    assert not _validate_input("123.A56.789-09")


@pytest.mark.parametrize(
    "doc, expected",
    [
        ("095482460", "15"),
        ("480995450", "10"),
    ],
)
def test_generate_first_digit(doc, expected):
    assert _generate_first_digit(doc) == expected[0]


@pytest.mark.parametrize(
    "doc, expected",
    [
        ("39053344705", "05"),  # Exemplo de CPF válido
        ("12345678909", "09"),  # Outro exemplo, atualize com um CPF válido
    ],
)
def test_generate_second_digit(doc, expected):
    assert _generate_second_digit(doc) == expected[1]


@pytest.mark.parametrize(
    "cpf, expected",
    [
        ("321.589.010-04", True),
        ("949.117.780-00", False),
        ("111.111.111-11", False),
        ("123.A56.789-09", False),
        ("84549854090", True),
        ("123.56.789-090000", False),
        ("03551921016", True),
    ],
)
def test_validate_cpf(cpf, expected):
    assert validate_cpf(cpf) == expected
