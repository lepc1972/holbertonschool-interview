#!/usr/bin/python3
"""Write a method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """
    Return True if all boxes can be opened.
    Otherwise, return False.
    """
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys:
                keys.append(box)
    return len(keys) == len(boxes)
