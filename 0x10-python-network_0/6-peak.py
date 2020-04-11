#!/usr/bin/python3
# Find a peak of list of unsorted integers


def find_peak(list_of_integers):
    """return the peak of a list"""

    max = 0

    if list_of_integers:
        for x in list_of_integers:
            if x > max:
                max = x
        return max
    else:
        return "None"
