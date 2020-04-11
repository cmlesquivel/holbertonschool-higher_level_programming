#!/usr/bin/python3
# Find a peak of list of unsorted integers

def find_peak(list_of_integers):
    """return the peak of a list"""

    if list_of_integers:
        return (max(list_of_integers))
    else:
        return ("None")
