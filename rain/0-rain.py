#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""


def rain(walls):
    """
    Calculate the amount of rainwater retained after it rains.

    Args:
        walls (list): List of non-negative integers representing wall heights.

    Returns:
        int: Total amount of rainwater retained.
    """
    if not walls or len(walls) < 3:
        return 0  # No water can be trapped if walls are empty or too short
    n = len(walls)
    left_max = [0] * n  # Max height to the left of each index
    right_max = [0] * n  # Max height to the right of each index
    # Fill left_max array
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])
    # Fill right_max array
    right_max[-1] = walls[-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])
    # Calculate water trapped
    total_water = 0
    for i in range(n):
        total_water += max(min(left_max[i], right_max[i]) - walls[i], 0)
    return total_water
