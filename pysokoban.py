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
import pygame  # Necessary.
import pygame.display
import pygame.time
import pygame.event
import sys  # sys.exit()
import movement as pysokoban_movement
import map_data as pysokoban_map_data
import surface as pysokoban_surface
from pygame.locals import *
from constants import *

level_counter = 0


def shutdown():
    pygame.quit()
    sys.exit()


def main(window_width, window_height, fps, file_name):
    surface = pygame.display.set_mode((window_width, window_height))
    surface.fill(BG_COLOR)
    pygame.display.set_caption('PySokoban')
    fps_clock = pygame.time.Clock()
    levels = pysokoban_map_data.load(file_name)
    player_location = levels[level_counter]['start_state']['player']
    map_data = levels[level_counter]['map_obj']
    map_surface = pysokoban_surface.get_surface(map_data, player_location)

    map_surface_rect = map_surface.get_rect()
    map_surface_rect.center = (window_width / 2, window_height / 2)
    # Event loop.
    while True:
        # Grab ALL events to process
        for event in pygame.event.get():
            if event.type == QUIT:
                shutdown()
            elif event.type == KEYUP:  # Pressed a key.
                direction = None
                if event.key == K_a:  # Left.
                    direction = LEFT
                elif event.key == K_d:  # Right
                    direction = RIGHT
                elif event.key == K_w:  # Up.
                    direction = UP
                elif event.key == K_d:  # Down.
                    direction = DOWN
                elif event.key == K_BACKSPACE:  # Undo.
                    pass
                elif event.key == K_SPACE:  # Redo.
                    pass
                    pysokoban_movement.move(direction, map_data, player_location)
        surface.blit(map_surface, map_surface_rect)
        pygame.display.update()
        fps_clock.tick(fps)


if __name__ == '__main__':
    main(window_width=800, window_height=600, fps=60, file_name='level/Default.pysl')
