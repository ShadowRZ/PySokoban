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


def load(file_name):
    map_file = open(file_name)
    content = map_file.readlines() + ['\r\n']
    map_file.close()

    # Levels.
    levels = []
    map_text_lines = []
    map_obj = []
    for line_num in range(len(content)):
        line = content[line_num].rstrip('\r\n')

        if ';' in line:
            # It is a comment.
            line = line[:line.find(';')]

        if line != '':
            # It is a part of map.
            map_text_lines.append(line)
        elif line == '' and len(map_text_lines) > 0:
            # A blank line indicates the end of a level's map in the file.
            # Find the longest row.
            max_width = -1
            for i in range(len(map_text_lines)):
                if len(map_text_lines[i]) > max_width:
                    max_width = len(map_text_lines[i])
                # Fill blanks with space.
            for i in range(len(map_text_lines)):
                map_text_lines[i] += ' ' * (max_width - len(map_text_lines[i]))

            # Convert.
            for x in range(len(map_text_lines[0])):
                map_obj.append([])
            for y in range(len(map_text_lines)):
                for x in range(max_width):
                    map_obj[x].append(map_text_lines[y][x])

            # Player location.
            start_x = None
            start_y = None
            goals = []
            crates = []
            for x in range(max_width):
                for y in range(len(map_obj[x])):
                    if map_obj[x][y] in ('@', '+'):
                        # '@' is player, '+' is player & goal
                        start_x = x
                        start_y = y
                    if map_obj[x][y] in ('.', '+', '*'):
                        # '.' is goal, '*' is star & goal
                        goals.append((x, y))
                    if map_obj[x][y] in ('$', '*'):
                        # '$' is star
                        crates.append((x, y))

            # Level check.
            assert start_x is not None and start_y is not None
            assert len(goals) > 0
            assert len(crates) >= len(goals)

            # Create level object.
            game_state = {'player': (start_x, start_y),
                          'step_counter': 0,
                          'crates': crates}
            level_obj = {'width': max_width,
                         'height': len(map_obj),
                         'map_obj': map_obj,
                         'goals': goals,
                         'start_state': game_state}

            levels.append(level_obj)

            # Reset.
            map_text_lines = []
            map_obj = []
    return levels


def get_block(map_data, x, y):
    return map_data[y][x]
