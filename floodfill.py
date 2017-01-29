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


def floodfill(map_data, map_surface, location):
    x = location[0]
    y = location[1]
    if not map_data[x + 1][y] in ('o', '#'):
        map_data[x + 1][y] = 'o'
        floodfill(map_data, map_surface, (x + 1, y))
    if not map_data[x - 1][y] in ('o', '#'):
        map_data[x - 1][y] = 'o'
        floodfill(map_data, map_surface, (x - 1, y))
    if not map_data[x][y + 1] in ('o', '#'):
        map_data[x][y + 1] = 'o'
        floodfill(map_data, map_surface, (x, y + 1))
    if not map_data[x][y - 1] in ('o', '#'):
        map_data[x][y - 1] = 'o'
        floodfill(map_data, map_surface, (x, y - 1))
