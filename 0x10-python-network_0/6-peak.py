#!/usr/bin/python3
""" Module for function find_peak """


def find_peak(list_of_integers):
    """
     Function finds the peak of a list of integers
        Arguments:
            list_of_integers - the list of numbers
    """
    if not list_of_integers or list_of_integers == []:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]
    return rec(list_of_integers, 0, len(list_of_integers))


def rec(list_of_integers, b, e):
    """ Recursive function to find peak of list_of_integers """
    if e - b < 2:
        return None
    mid = (b + e) // 2
    if list_of_integers[mid] > list_of_integers[
            mid - 1] and list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]
    return rec(list_of_integers, mid, e) or rec(list_of_integers, b, mid)
