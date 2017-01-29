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


def move(direction, map_data, player_location):
    x = player_location[0]
    y = player_location[1]
    if move_able(map_data, player_location, direction):
        if direction == UP:
            map_data[x][y] = ' '
            if map_data[x][y - 1] == '$':
                map_data[x][y - 1] = ' '
                if map_data[x][y - 2] == '.':
                    map_data[x][y - 2] = '*'
                else:
                    map_data[x][y - 2] = '$'
            map_data[x][y - 1] = '@'
            player_location[1] -= 1
        elif direction == DOWN:
            map_data[x][y] = ' '
            if map_data[x][y + 1] == '$':
                map_data[x][y + 1] = ' '
                if map_data[x][y + 2] == '.':
                    map_data[x][y + 2] = '*'
                else:
                    map_data[x][y + 2] = '$'
            map_data[x][y + 1] = '@'
            player_location[1] += 1
        elif direction == LEFT:
            map_data[x][y] = ' '
            if map_data[x - 1][y] == '$':
                map_data[x - 1][y] = ' '
                if map_data[x - 2][y] == '.':
                    map_data[x - 2][y] = '*'
                else:
                    map_data[x - 2][y] = '$'
            map_data[x - 1][y] = '@'
            player_location[0] -= 1
        elif direction == RIGHT:
            map_data[x][y] = ' '
            if map_data[x + 1][y] == '$':
                map_data[x + 1][y] = ' '
                if map_data[x + 2][y] == '.':
                    map_data[x + 2][y] = '*'
                else:
                    map_data[x + 2][y] = '$'
            map_data[x + 1][y] = '@'
            player_location[0] += 1


def move_able(map_data, location, direction):
    x = location[0]
    y = location[1]
    if direction == UP:
        if map_data[x][y - 1] in (' ', '.'):
            return True
        elif map_data[x][y - 1] in ('$', '*'):
            return map_data[x][y - 2] in (' ', '.')
    elif direction == DOWN:
        if map_data[x][y + 1] in (' ', '.'):
            return True
        elif map_data[x][y + 1] in ('$', '*'):
            return map_data[x][y + 2] in (' ', '.')
    elif direction == LEFT:
        if map_data[x - 1][y] in (' ', '.'):
            return True
        elif map_data[x - 1][y] in ('$', '*'):
            return map_data[x - 2][y] in (' ', '.')
    elif direction == RIGHT:
        if map_data[x + 1][y] in (' ', '.'):
            return True
        elif map_data[x + 1][y] in ('$', '*'):
            return map_data[x - 2][y] in (' ', '.')
    return False
