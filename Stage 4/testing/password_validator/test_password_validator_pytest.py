from password_validator import validate_password


def test_valid_password():
    assert validate_password("Python@123") is True


def test_no_uppercase():
    assert validate_password("python@123") is False


def test_no_digit():
    assert validate_password("Python@abc") is False


def test_too_short():
    assert validate_password("Py@12") is False


def test_no_special_character():
    assert validate_password("Python123") is False