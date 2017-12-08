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

"""Manages all physics.
"""
from typing import Tuple
from enum import Enum


class ForceType(Enum):
    """Type of force that can be applied to physical objects.
    """
    IMPULSE = 0


class PhysicalObject:
    """Physical object in the physics engine.
    This is anything that can move or be interacted with in any physical way.

    === Public Attributes ===
    density:
        density of this object in kg/m^2

    position:
        (x, y) tuple coordinates of where the object's center is in floats
    velocity:
        (x, y) tuple velocity of this object in m/s
    rotation:
        rotation of this object in degrees
        counting clockwise from positive y-axis
    rotational_velocity:
        rotational velocity of this object where clockwise is positive

    is_static:
        whether or not this object is static (i.e. unmovable)
    is_active:
        whether or not this object is active in the engine
    """
    density: float
    position: Tuple[float, float]
    velocity: Tuple[float, float]
    rotation: float
    rotational_velocity: float
    is_static: bool
    is_active: bool

    def __init__(self, density: float,
                 position: Tuple[float, float] = (0, 0), rotation: float = 0,
                 is_static: bool = False) -> None:
        """Initialize this physical object.
        """
        self.density = density
        self.position = position
        self.velocity = (0, 0)
        self.rotation = rotation
        self.rotational_velocity = 0
        self.is_static = is_static
        self.is_active = True

    def get_area(self) -> float:
        """Calculate the area of this physical object.

        Returns a float representing the area in m^2.
        """
        raise NotImplementedError

    def get_mass(self) -> float:
        """Calculate the mass of this physical object.

        Returns a float representing the mass in kg.
        """
        return self.get_area() * self.density

    def add_force(self, force: float,
                  force_type: int = ForceType.IMPULSE) -> None:
        """Add a force to this object of magnitude <force> with type of force
        <force_type>.
        """
        # TODO: implement
        pass
