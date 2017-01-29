#!/usr/bin/env python

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
    is_started = False
    # Surfaces
    surface = pygame.display.set_mode((window_width, window_height))
    surface.fill(BG_COLOR)
    pygame.display.set_caption("PySokoban - Press Space to start!")
    # Clock.
    fps_clock = pygame.time.Clock()
    # Draw title.
    # noinspection PyUnresolvedReferences
    title_surface = pygame.image.load("title.png")
    title_surface_rect = title_surface.get_rect()
    title_surface_rect.center = (window_width / 2, window_height / 2)
    surface.blit(title_surface, title_surface_rect)
    pygame.display.update()
    # First loop to show a splash screen.
    while not is_started:
        for e in pygame.event.get():
            if e.type == QUIT:
                shutdown()
            elif e.type == KEYUP:  # Pressed a key.
                if e.key == K_SPACE:
                    is_started = True
    surface.fill(BG_COLOR)
    pygame.display.set_caption("PySokoban - Level {}, Steps:{}".format(level_counter, 0))
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
                        # Add a step to step counter.
                        game_state['step_counter'] += 1
                        redraw = True

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

                # Level is complete.
                if pysokoban_level_check.level_is_complete(crates, goals):
                    level_counter += 1
                    # Set to next level.
                    level = levels[level_counter]
                    game_state = level['start_state']
                    player_location = game_state['player']
                    crates = game_state['crates']
                    map_data = level['map_obj']
                    goals = level['goals']
                    # Blit refreshed surface.
                    surface.blit(map_surface, map_surface_rect)
                    level_complete_blit(surface, window_height, window_width)
                    pygame.display.update()
                    exit_flag = False
                    while not exit_flag:
                        for e in pygame.event.get():
                            if e.type == QUIT:
                                shutdown()
                            elif e.type == KEYUP:  # Pressed a key.
                                if e.key == K_SPACE:
                                    exit_flag = True

                    # Redraw second time..
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

        pygame.display.set_caption("PySokoban - Level {}, Steps:{}"
                                   .format(level_counter + 1, game_state['step_counter']))
        # Blit surface and update.
        surface.blit(map_surface, map_surface_rect)
        pygame.display.update()
        fps_clock.tick(fps)


def level_complete_blit(surface, window_height, window_width):
    """
    Blit level complete image.
    :param surface:
    :param window_height:
    :param window_width:
    """
    pygame.display.set_caption("PySokoban - Level Complete! Press Space to go to next level!")
    # Blit level complete image.
    # noinspection PyUnresolvedReferences
    title_surface = pygame.image.load("complete.png")
    title_surface_rect = title_surface.get_rect()
    title_surface_rect.center = (window_width / 2, window_height / 2)
    surface.blit(title_surface, title_surface_rect)
    pygame.display.update()


if __name__ == '__main__':
    # noinspection SpellCheckingInspection
    file_string = "level/Default.pysl"
    if sys.argv[0] == '':
        file_string = sys.argv[0]
    assert os.path.exists(file_string)
    main(window_width=800, window_height=600, fps=60, file_name=file_string, camera_offset=32)
