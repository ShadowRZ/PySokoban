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
import copy

import pygame

from constants import *


def get_surface(map_data, player_location, crates, goals):
    """
    Gets a surface of the map.
    :param map_data:
    :param player_location:
    :param crates:
    :param goals:
    :return: A surface of map.
    """
    map_height = len(map_data) * TILE_HEIGHT
    map_width = len(map_data[0]) * TILE_WIDTH
    ret = pygame.Surface((map_width, map_height))
    ret.fill(BG_COLOR)

    data_copy = copy.deepcopy(map_data)
    # Floodfill up
    floodfill(data_copy, player_location)

    for x in range(len(data_copy)):
        for y in range(len(data_copy[0])):
            if data_copy[x][y] in BLOCK_MAP:
                ret.blit(BLOCK_MAP[data_copy[x][y]], (x * TILE_WIDTH, y * TILE_HEIGHT))
    for crate in crates:
        ret.blit(BLOCK_MAP['$'], (crate[0] * TILE_WIDTH, crate[1] * TILE_HEIGHT))
    for goal in goals:
        ret.blit(BLOCK_MAP['.'], (goal[0] * TILE_WIDTH, goal[1] * TILE_HEIGHT))
    ret.blit(pygame.image.load(PLAYER_DOWN), (player_location[0] * TILE_WIDTH, player_location[1] * TILE_HEIGHT))
    return ret


def floodfill(map_data, location):
    """
    Flood-fill the map.
    :param map_data: Map data
    :param location:
    """
    x = location[0]
    y = location[1]
    if not map_data[x + 1][y] in ('o', '#'):
        map_data[x + 1][y] = 'o'
        floodfill(map_data, (x + 1, y))
    if not map_data[x - 1][y] in ('o', '#'):
        map_data[x - 1][y] = 'o'
        floodfill(map_data, (x - 1, y))
    if not map_data[x][y + 1] in ('o', '#'):
        map_data[x][y + 1] = 'o'
        floodfill(map_data, (x, y + 1))
    if not map_data[x][y - 1] in ('o', '#'):
        map_data[x][y - 1] = 'o'
        floodfill(map_data, (x, y - 1))
