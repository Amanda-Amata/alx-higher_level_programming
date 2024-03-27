#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers
    THOUGHT PROCESS
        it is not sorted, sorting would take n(log(n))
            -> not worth sorting
        looping through and keeping track of max (brute force)
            -> O(n)
        possibly looping from each end reducing to 1/2 run time
            -> still O(n)
"""

def find_peak(list_of_integers):
    """BRUTE force implementation for question
    """
    max_i = None
    for ele in list_of_integers:
        if max_i is None or max_i < ele:
            max_i = ele
    return max_i
