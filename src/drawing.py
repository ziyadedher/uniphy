# This file is part of UniPhy.
#
# UniPhy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# UniPhy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with UniPhy.  If not, see <http://www.gnu.org/licenses/>.

"""Manages all forms of drawing from objects to text.
"""
from typing import Tuple, List

import arcade

from src import physics


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
        """Initialize this window.
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


class ObjectDrawer:
    """Manages all object drawing to the window.
    """
    # === Private Attributes ===
    # _objects:
    #   list of all physics objects
    _objects: List[physics.PhysicalObject]

    def __init__(self) -> None:
        """Initializes this drawer.
        """
        self._objects = []

    def register_object(self, object: physics.PhysicalObject) -> None:
        """Register a physics object into the drawer.
        """
        # TODO: implement
        pass

    def purge_inactive_objects(self) -> None:
        """Remove all inactive objects from drawing.
        """
        # TODO: implement
        pass

    def draw(self) -> None:
        """Draws all objects.
        """
        # TODO: implement
        pass
