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
from pygame.locals import *


def shutdown():
    pygame.quit()
    sys.exit()


def main(window_width, window_height, fps):
    pygame.init()
    surface = pygame.display.set_mode((window_width, window_height), 0, 32)
    pygame.display.set_caption('PySokoban')
    fps_clock = pygame.time.Clock()
    # Event loop.
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                shutdown()
            elif event.type == KEYUP:
                if event.key == K_a:
                    pass
                elif event.key == K_d:
                    pass
                elif event.key == K_w:
                    pass
                elif event.key == K_d:
                    pass
                elif event.key == K_BACKSPACE:  # Undo.
                    pass
                elif event.key == K_SPACE:  # Redo.
                    pass


if __name__ == '__main__':
    main(window_width=800, window_height=600, fps=60)
