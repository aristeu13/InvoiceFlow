from src.core.common.fake_person import generate_cpf, generate_name
from src.core.common.validates import (
    validate_cpf,
)


def test_generate_cpf():
    assert validate_cpf(generate_cpf()) is True


def test_generate_name():
    generated_name = generate_name()
    assert generated_name is not None
    assert generated_name != ""
    assert len(generated_name) >= 3
