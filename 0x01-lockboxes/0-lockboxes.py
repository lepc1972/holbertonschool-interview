#!/usr/bin/python3
"""Method to check if all boxes can be openned"""


def canUnlockAll(boxes):
    """Method to chek if the boxes can be openned"""
    for key in range(1, len(boxes) - 1):
        boxes_checked = False

        for index in range(len(boxes)):
            if key in boxes[index] and key != index:
                boxes_checked = True
                break

        if boxes_checked is False:
            return False

    return True
