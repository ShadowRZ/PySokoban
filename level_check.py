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


def level_is_complete(crates, goals):
    # type: (list, list) -> bool
    """
    Check if a level is complete.
    :rtype: bool
    :param crates: A list of crates.
    :param goals: A list of goals.
    :return: True if a level is completed.
    """
    for goal in goals:
        if goal not in crates:
            return False
    return True
