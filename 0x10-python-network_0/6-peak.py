#!/usr/bin/python3
# Find a peak of list of unsorted integers


def find_peak(list_of_integers):
    """return the peak of a list"""

    max = 0
    if list_of_integers:
        b = len(list_of_integers) - 1

        for x in range(len(list_of_integers)):
            if list_of_integers[x] > max:
                max = list_of_integers[x]
            if list_of_integers[b] > max:
                max = list_of_integers[b]
            if x >= b:
                return max
            else:
                b = b - 1
    else:
        return "None"
