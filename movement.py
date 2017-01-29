# This file is a part of PySokoban.
# Copyright (C) 2017 @ShadowRZ (HID_System)
# PySokoban is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from constants import *


def move(direction, map_data, player_location, crates):
    # type: (str, list, list, list) -> bool
    """
    Given a map and game state object, see if it is possible for the
    player to make the given move. If it is, then change the player's
    position (and the position of any pushed star). If not, do nothing.
    :rtype: bool
    :param direction: Direction to move.
    :param map_data: Map Data
    :param player_location: Player location.
    :param crates: Crate locations.
    :return True if the player moved, otherwise False.
    """
    x = player_location[0]
    y = player_location[1]
    x_offset = 0
    y_offset = 0
    if direction == UP:
        y_offset -= 1
    elif direction == DOWN:
        y_offset += 1
    elif direction == LEFT:
        x_offset -= 1
    elif direction == RIGHT:
        x_offset += 1
    if is_wall(map_data, x + x_offset, y + y_offset):
        return False
    else:
        if (x + x_offset, y + y_offset) in crates:
            # There is a crate.
            if not is_blocked(map_data, x + x_offset * 2, y + y_offset * 2, crates):
                # Move the crate.
                index = crates.index((x + x_offset, y + y_offset))
                crates[index] = (crates[index][0] + x_offset, crates[index][1] + y_offset)
            else:
                return False
        player_location[0] += x_offset
        player_location[1] += y_offset


def is_wall(map_data, x, y):
    # type: (list, int, int) -> bool
    """
    Check if it is wall.
    :param map_data: Map data.
    :param x: X to check.
    :param y: Y to check.
    :return: True if it is wall. False otherwise.
    :rtype: bool
    """
    if x < 0 or x >= len(map_data) or y < 0 or y >= len(map_data[x]):
        # Out of range.
        return False
    elif map_data[x][y] == '#':
        # It is.
        return True
    return False


def is_blocked(map_data, x, y, crates):
    # type: (list, int, int, list) -> bool
    """
    Check if it is blocked.
    :rtype: bool
    :param map_data: Map data
    :param x: X to check.
    :param y: Y to check.
    :param crates: Crate locations
    :return: True if it is blocked, False otherwise.
    """
    if is_wall(map_data, x, y):
        # Blocked by wall.
        return True
    elif x < 0 or x >= len(map_data) or y < 0 or y >= len(map_data[x]):
        # Out of range.
        return False
    elif (x, y) in crates:
        # Blocked by crates.
        return True
