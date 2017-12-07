"""Test user entry point to the program.
"""
import base  # noqa # pylint: disable=unused-import
import uniphy


def test_print_welcome() -> None:
    """Test printing welcome statement.
    """
    assert uniphy.print_welcome() is None


def test_print_license() -> None:
    """Test printing license disclaimer.
    """
    assert uniphy.print_license() is None


def test_main() -> None:
    """Test the main holder.
    """
    assert uniphy.main() is None
