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
import sys  # sys.exit()

import pygame.display
import pygame.event
import pygame.time
from pygame.locals import *

import level_check as pysokoban_level_check
import map_data as pysokoban_map_data
import movement as pysokoban_movement
import surface as pysokoban_surface
from constants import *


def shutdown():
    pygame.quit()
    sys.exit()


def main(window_width, window_height, fps, file_name, camera_offset):
    """
    Main function.
    :param camera_offset: Camera offset.
    :param window_width: Window width.
    :param window_height: Window height
    :param fps: Frames per second
    :param file_name: File to load.
    """
    # Start up.
    level_counter = 0
    # Surfaces
    surface = pygame.display.set_mode((window_width, window_height))
    surface.fill(BG_COLOR)
    pygame.display.set_caption('PySokoban')
    # Clock.
    fps_clock = pygame.time.Clock()
    # Level data.
    levels = pysokoban_map_data.load(file_name)
    level = levels[level_counter]

    game_state = level['start_state']
    player_location = game_state['player']
    crates = game_state['crates']
    map_data = level['map_obj']
    goals = level['goals']

    # Map surface.
    map_surface = pysokoban_surface.get_surface(map_data, player_location, crates, goals)

    map_surface_rect = map_surface.get_rect()
    map_surface_rect.center = (window_width / 2, window_height / 2)

    camera_x_offset = 0  # Camera X offset.
    camera_y_offset = 0  # Camera Y offset.
    # Event loop.
    while True:
        # Grab ALL events to process
        for event in pygame.event.get():
            if event.type == QUIT:
                shutdown()
            elif event.type == KEYUP:  # Pressed a key.
                direction = None  # Direction.
                redraw = False  # Requires redraw.
                if event.key == K_a:  # Left.
                    direction = LEFT
                    redraw = True
                    camera_x_offset += camera_offset
                elif event.key == K_d:  # Right
                    direction = RIGHT
                    redraw = True
                    camera_x_offset -= camera_offset
                elif event.key == K_w:  # Up.
                    direction = UP
                    redraw = True
                    camera_y_offset += camera_offset
                elif event.key == K_s:  # Down.
                    direction = DOWN
                    redraw = True
                    camera_y_offset -= camera_offset
                elif event.key == K_BACKSPACE:  # Undo.
                    pass
                elif event.key == K_SPACE:  # Redo.
                    pass

                # If moved and level is not complete.
                if direction is not None:
                    # Player make a move.
                    moved = pysokoban_movement.move(direction, map_data, player_location, crates)
                    if moved:
                        game_state['step_counter'] += 1
                        redraw = True

                # Level is complete.
                if pysokoban_level_check.level_is_complete(crates, goals):
                    redraw = True
                    level_counter += 1
                    # Set to next level.
                    level = levels[level_counter]
                    game_state = level['start_state']
                    player_location = game_state['player']
                    crates = game_state['crates']
                    map_data = level['map_obj']
                    goals = level['goals']
                if redraw:  # Redraw.
                    # First fill with background color.
                    surface.fill(BG_COLOR)
                    # Get the surface.
                    map_surface = pysokoban_surface.get_surface(map_data, player_location, crates, goals)
                    # Get the rectangle of map surface.
                    map_surface_rect = map_surface.get_rect()
                    # If the width of map surface is smaller than screen surface
                    if map_surface_rect.width < window_width:
                        camera_x_offset = 0
                    if map_surface_rect.height < window_height:
                        camera_y_offset = 0
                    # Re-set center of map surface's rectangle.
                    map_surface_rect.center = (window_width / 2 + camera_x_offset, window_height / 2 + camera_y_offset)
        # Blit surface and update.
        surface.blit(map_surface, map_surface_rect)
        pygame.display.update()
        fps_clock.tick(fps)


if __name__ == '__main__':
    # noinspection SpellCheckingInspection
    main(window_width=800, window_height=600, fps=60, file_name='level/Default.pysl', camera_offset=32)
