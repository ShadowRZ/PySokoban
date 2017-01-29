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
import pygame
import copy
import floodfill as pysokoban_floodfill
from constants import *


def get_surface(map_data, player_location):
    map_height = len(map_data)
    map_width = len(map_data[0])
    ret = pygame.Surface((map_width * TILE_WIDTH, map_height * TILE_HEIGHT))
    ret.fill(BG_COLOR)

    data_copy = copy.deepcopy(map_data)
    # Floodfill up
    pysokoban_floodfill.floodfill(data_copy, ret, player_location)

    for x in range(len(data_copy[0])):
        for y in range(len(data_copy)):
            if data_copy[x][y] in BLOCK_MAP:
                ret.blit(BLOCK_MAP[data_copy[x][y]], (x * TILE_WIDTH, y * TILE_HEIGHT))

    for x in range(len(map_data[0])):
        for y in range(len(map_data)):
            if map_data[x][y] in BLOCK_MAP:
                ret.blit(BLOCK_MAP[map_data[x][y]], (x * TILE_WIDTH, y * TILE_HEIGHT))
            elif map_data[x][y] == '+':  # + is player & goal
                # Blit player, then goal.
                ret.blit(BLOCK_MAP['@'], (x * TILE_WIDTH, y * TILE_HEIGHT))
                ret.blit(BLOCK_MAP['.'], (x * TILE_WIDTH, y * TILE_HEIGHT))
            elif map_data[x][y] == '*':  # * is crate & goal
                # Blit goal, then crate.
                ret.blit(BLOCK_MAP['.'], (x * TILE_WIDTH, y * TILE_HEIGHT))
                ret.blit(BLOCK_MAP['$'], (x * TILE_WIDTH, y * TILE_HEIGHT))
    return ret
