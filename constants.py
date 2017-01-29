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
import os

import pygame.image

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

TILE_WIDTH = 64
TILE_HEIGHT = 64

BLOCK_FILE = 'image/block_07.png'
CRATE_FILE = 'image/crate_18.png'
END_POINT_FILE = 'image/environment_06.png'
GROUND_FILE = 'image/ground_01.png'

PLAYER_DOWN = 'image/player_05.png'
PLAYER_UP = 'image/player_08.png'
PLAYER_LEFT = 'image/player_20.png'
PLAYER_RIGHT = 'image/player_17.png'

assert os.path.exists(BLOCK_FILE) \
       and os.path.exists(CRATE_FILE) \
       and os.path.exists(END_POINT_FILE) \
       and os.path.exists(GROUND_FILE) \
       and os.path.exists(PLAYER_DOWN) \
       and os.path.exists(PLAYER_UP) \
       and os.path.exists(PLAYER_LEFT) \
       and os.path.exists(PLAYER_RIGHT)

BLOCK_MAP = {'#': pygame.image.load(BLOCK_FILE),
             '.': pygame.image.load(END_POINT_FILE),
             '$': pygame.image.load(CRATE_FILE),
             '@': pygame.image.load(PLAYER_DOWN),
             'o': pygame.image.load(GROUND_FILE)}

BG_COLOR = (89, 106, 108)
