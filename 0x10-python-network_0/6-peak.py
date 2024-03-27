#!/usr/bin/python3
"""  function that finds a peak in a list of unsorted integers
    Args:
        list_of_integers: A list of unsorted integers
    Returns:
        The peak element in the list of integers.
"""

def find_peak(list_of_integers):
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    middle_indx = int(len(list_of_integers) / 2)

    if middle_indx != len(list_of_integers) - 1:
        if list_of_integers[middle_indx - 1] < list_of_integers[middle_indx] and\
            list_of_integers[middle_indx + 1] < list_of_integers[middle_indx]:
            return list_of_integers[middle_indx]
        elif list_of_integers[middle_indx] == list_of_integers[middle_indx + 1]:
            return list_of_integers[middle_indx]
    else:
        if list_of_integers[middle_indx - 1] < list_of_integers[middle_indx]:
            return list_of_integers[middle_indx]
        else:
            return list_of_integers[middle_indx - 1]

    if list_of_integers[middle_indx - 1] > list_of_integers[middle_indx]:
        a_list = list_of_integers[0:middle_indx]
    else:
        a_list = list_of_integers[middle_indx + 1:]

    return find_peak(a_list)
