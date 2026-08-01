import unittest
from password_validator import validate_password


class TestPasswordValidator(unittest.TestCase):

    def test_valid_password(self):
        self.assertTrue(validate_password("Python@123"))

    def test_no_uppercase(self):
        self.assertFalse(validate_password("python@123"))

    def test_no_digit(self):
        self.assertFalse(validate_password("Python@abc"))

    def test_too_short(self):
        self.assertFalse(validate_password("Py@12"))

    def test_no_special_character(self):
        self.assertFalse(validate_password("Python123"))


if __name__ == "__main__":
    unittest.main()