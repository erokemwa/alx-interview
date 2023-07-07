#!/usr/bin/python3
"""
Method that determines if all the boxes can be opened.
Given n number of locked boxes, each box numbered sequentially
from 0 to n - 1, and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    - boxes: A list of lists representing the boxes and their keys.

    Returns:
    - True if all the boxes can be opened, False otherwise.
    """
    if not boxes or type(boxes) is not list:
        # Invalid input: empty or non-list boxes
        return False

    unlocked = [0]  # List of unlocked boxes

    # Traverse the unlocked boxes
    for x in unlocked:
        # Check the keys in the current box
        for y in boxes[x]:
            if y not in unlocked and y < len(boxes):
                # Found a new key, add it to unlocked list
                unlocked.append(y)

    # Check if all boxes are unlocked
    if len(unlocked) == len(boxes):
        return True
    return False

