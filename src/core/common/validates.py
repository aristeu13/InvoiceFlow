# validate_cpf is from:
# Source: https://github.com/alvarofpp/validate-docbr/blob/main/validate_docbr/CPF.py


def _validate_input(input: str) -> bool:
    """
    Validate input.
    If it has only digits and valid characters, return True.
    If it has any character that is not a digit or valid character, return False.
    """
    valid_characters = [".", "-"]

    set_non_digit_characters = set([x for x in input if not x.isdigit()])
    set_valid_characters = set(valid_characters)

    return len(set_non_digit_characters.difference(set_valid_characters)) <= 0


def _generate_first_digit(doc: str) -> str:
    """Generate the first CPF verification digit."""
    _sum = 0

    for i in range(10, 1, -1):
        _sum += int(doc[10 - i]) * i

    _sum = (_sum * 10) % 11

    if _sum == 10:
        _sum = 0

    return str(_sum)


def _generate_second_digit(doc: str) -> str:
    """Generate the second CPF verification digit."""
    _sum = 0

    for i in range(11, 1, -1):
        _sum += int(doc[11 - i]) * i

    _sum = (_sum * 10) % 11

    if _sum == 10:
        _sum = 0

    return str(_sum)


def validate_cpf(cpf: str) -> bool:
    """Validate CPF."""
    if not _validate_input(cpf):
        return False

    # Remove some unwanted characters
    cpf = list("".join([x for x in cpf if x.isdigit()]))

    if len(cpf) != 11:
        return False

    if len(set(cpf)) == 1:
        return False

    return (
        _generate_first_digit(cpf) == cpf[9] and _generate_second_digit(cpf) == cpf[10]
    )
