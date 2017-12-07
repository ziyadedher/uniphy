"""Manages all forms of drawing from objects to text.
"""
from typing import Tuple

import arcade


# Window constants
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
SCREEN_TITLE = "UniPhy Standalone"
BACKGROUND_COLOR = arcade.color.BLACK


class Window(arcade.Window):
    """Main drawing window.

    Handles all window events.
    """
    def __init__(self, width: int, height: int, title: str,
                 background_color: Tuple[int, int, int]) -> None:
        """Initializes this window.
        """
        # Initializes the arcade screen and sets background color
        # TODO: implement resizing
        super().__init__(width, height, title)
        arcade.set_background_color(background_color)

    def update(self, delta_time) -> None:
        """Called before every frame.

        <delta_time> is the time elapsed since last call.
        """
        # TODO: call all updating of physics
        pass

    def on_draw(self) -> None:
        """Called to render the screen.
        """
        # Clear the screen
        arcade.start_render()

        # TODO: call all drawing
        pass

    def on_mouse_press(self, x: float, y: float,
                       button: int, modifiers: int) -> None:
        """Called on any mouse down.
        """
        # TODO: call all mouse press actions
        pass

    def on_mouse_release(self, x: float, y: float,
                         button: int, modifiers: int) -> None:
        """Called on any mouse up.
        """
        # TODO: call all mouse release actions
        pass

    def on_mouse_scroll(self, x: int, y: int,
                        scroll_x: int, scroll_y: int) -> None:
        """Called when mouse wheel is scrolled.
        """
        # TODO: call all mouse scroll actions
        pass

    def on_mouse_motion(self, x: float, y: float,
                        dx: float, dy: float) -> None:
        """Called when mouse is moved.
        """
        # TODO: call all mouse move actions
        pass

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        """Called on any key down.
        """
        # TODO: call all key press actions
        pass

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        """Called on any key up.
        """
        # TODO: call all key release actions
        pass
