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

"""Entry point to the program. Handles direct use of uniphy.
"""


def main() -> None:
    """Runs uniphy standalone.
    """
    print_license()
    print_welcome()


def print_license() -> None:
    """Prints the license disclaimer to console.
    """
    print("This program is distributed under the GPLv3.")
    print("Copyright 2017 Ziyad Edher.")
    print("")


def print_welcome() -> None:
    """Prints a welcome message to console.
    """
    print("Welcome to UniPhy standalone.")
    print("")


if __name__ == '__main__':
    main()
