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

"""Manages creating physics objects and editing them.
"""
from typing import Tuple

from src import physics


class Builder:
    """Builds physics objects passing them to be drawn and created.
    """

    # === Private Attribute ===
    # _is_building:
    #   whether or not there is a physical object currently being built
    # _pos:
    #   position of the center of the physical object currently being built
    # _size:
    #   size of the physical object currently being built
    _is_building: bool
    _pos: Tuple[float, float]
    _size: float

    def __init__(self) -> None:
        """Initialize this builder.
        """
        self._is_building = False
        self._pos = (0, 0)
        self._size = 0

    def start_create(self, pos_x, pos_y) -> None:
        """Start creating a physics object.
        """
        # TODO: implement
        pass

    def update(self) -> None:
        """Update the current physical object being built.
        """
        # TODO: implement
        pass

    def draw(self) -> None:
        """Draw the current physical object being built.
        """
        # TODO: implement
        pass

    def end_create(self) -> physics.PhysicalObject:
        """End creating a physics object and returns the object.
        """
        # TODO: implement
        pass
