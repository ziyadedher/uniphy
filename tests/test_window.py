"""Test Window class.
"""
import base  # noqa # pylint: disable=unused-import
import arcade
from src import drawing


# Running constants
RUNNING_TIME = 0.1


def test_window_creation() -> None:
    """Test window does not crash when created.
    """
    window = drawing.Window(drawing.SCREEN_WIDTH, drawing.SCREEN_HEIGHT,
                            drawing.SCREEN_TITLE, drawing.BACKGROUND_COLOR)
    assert window.get_size() == (drawing.SCREEN_WIDTH, drawing.SCREEN_HEIGHT)


def test_arcade_running() -> None:
    """Test arcade does not crash when run.
    """
    window = drawing.Window(drawing.SCREEN_WIDTH, drawing.SCREEN_HEIGHT,
                            drawing.SCREEN_TITLE, drawing.BACKGROUND_COLOR)
    arcade.set_window(window)
    arcade.quick_run(RUNNING_TIME)
