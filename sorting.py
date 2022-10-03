"""
A module to hold sorting algorithms that also provide sorting steps for
visualization.

Author: Jacob Dentes
Date: 13 October 2021
"""


def step_quicksort(l, s_list=[], lo=0, hi=None):
    """
    Returns a sorted copy of the list. Modifies the step_list in place with
    the steps of the sort if it is provided.

    This function implements a modified Quicksort algorithm by Tony Hoare

    Paramter l: The list to sort
    Precondition: l is a list with comparable elements

    Parameter step_list: The list to contain steps of the sort. They represent
    any changes made at a given step, a tuple of (origin index, new index)
    Precondition: step_list is a list

    Parameter lo: The lower bound to sort from.
    Precondition: lo is an int, 0 <= off < len(l), and lo <= hi

    Parameter hi: The upper bound to sort from.
    Precondition: hi is None or an int with 0 <= off < len(l), and lo <= hi
    """
    l=l[:]
    if hi is None:
        hi = len(l)-1
    if len(l[lo:hi+1]) < 2:
        return l
    pivot = l[hi]
    added = 0
    for i in range(hi,lo-1,-1):
        if l[i]>pivot:
            s_list.append((i,hi))
            l.insert(hi,l.pop(i))
            hi -= 1
            added+=1
        else:
            s_list.append((i,i))
    return (step_quicksort(l,s_list,lo,hi-1)[:hi]+[pivot]+
            step_quicksort(l,s_list,hi+1,hi+added)[hi+1:])


def step_mergesort(l, s_list=[]):
    """
    Returns a sorted copy of the list. Modifies the step_list in place with
    the steps of the sort if it is provided.

    This function implements a modified Mergesort algorithm by John von Neumann

    Paramter l: The list to sort
    Precondition: l is a list with comparable elements

    Parameter step_list: The list to contain steps of the sort. They represent
    any changes made at a given step, a tuple of (origin index, new index)
    Precondition: step_list is a list
    """
    def mergesort(l, s_list=[], lo=0, hi=None):
        def merge(l,s_list,lo1,hi1,lo2,hi2):
            r_index = hi2
            for i in range(hi1,lo1-1,-1):
                while l[r_index] >= l[i] and not (lo2 > hi2):
                    l.insert(i+1,l.pop(r_index))
                    s_list.append((r_index,i+1))
                    lo2 += 1
                else:
                    s_list.append((i,i))
                if lo2 > hi2:
                    break
            else:
                while lo2 <= hi2:
                    l.insert(lo1,l.pop(r_index))
                    s_list.append((r_index,lo1))
                    lo2 += 1
        if hi is None:
            hi = len(l)-1
        if len(l[lo:hi+1]) < 2:
            return l
        lo1 = lo
        hi1 = lo+(len(l[lo:hi+1])//2)-1
        lo2 = hi1+1
        hi2 = lo2+len(l[lo2:hi])
        mergesort(l,s_list,lo1,hi1)
        mergesort(l,s_list,lo2,hi2)

        merge(l,s_list,lo1,hi1,lo2,hi2)
    return_l = l[:]
    mergesort(return_l,s_list)
    return return_l


def step_bubblesort(l,s_list=[]):
    """
    Returns a sorted copy of the list. Modifies the step_list in place with
    the steps of the sort if it is provided.

    This function implements a modified Bubble sort algorithm

    Paramter l: The list to sort
    Precondition: l is a list with comparable elements

    Parameter step_list: The list to contain steps of the sort. They represent
    any changes made at a given step, a tuple of (origin index, new index)
    Precondition: step_list is a list
    """
    l=l[:]
    highest = len(l) - 1
    while highest > 0:
        swaps = 0
        for i in range(highest):
            if l[i] > l[i+1]:
                l.insert(i+1,l.pop(i))
                s_list.append((i,i+1))
                swaps += 1
            else:
                s_list.append((i,i))
        highest -= 1
        if swaps == 0:
            break
    return l


def step_insertion_sort(l,s_list=[]):
    """
    Returns a sorted copy of the list. Modifies the step_list in place with
    the steps of the sort if it is provided.

    This function implements a modified insertion sort algorithm

    Paramter l: The list to sort
    Precondition: l is a list with comparable elements

    Parameter step_list: The list to contain steps of the sort. They represent
    any changes made at a given step, a tuple of (origin index, new index)
    Precondition: step_list is a list
    """
    l = l[:]
    part = len(l)-1
    while part >= 0:
        for j in range(part,len(l)):
            if l[part] < l[j]:
                l.insert(j-1,l.pop(part))
                s_list.append((part,j-1))
                break
            s_list.append((j,j))
        else:
            l.insert(len(l),l.pop(part))
            s_list.append((part,len(l)))
        part -= 1
    return l


def step_selection_sort(l,s_list=[]):
    """
    Returns a sorted copy of the list. Modifies the step_list in place with
    the steps of the sort if it is provided.

    This function implements a modified selection sort algorithm

    Paramter l: The list to sort
    Precondition: l is a list with comparable elements

    Parameter step_list: The list to contain steps of the sort. They represent
    any changes made at a given step, a tuple of (origin index, new index)
    Precondition: step_list is a list
    """
    l=l[:]
    hi=len(l)
    while hi > 0:
        max_i = (0, l[0])
        for i in range(0,hi):
            if l[i] > max_i[1]:
                max_i = (i,l[i])
            s_list.append((i,i))
        l.insert(hi-1,l.pop(max_i[0]))
        s_list.append((max_i[0],hi-1))
        hi -= 1
    return l


def step_cocktail_shaker(l,s_list=[]):
    """
    Returns a sorted copy of the list. Modifies the step_list in place with
    the steps of the sort if it is provided.

    This function implements a modified Cocktail shaker sort algorithm

    Paramter l: The list to sort
    Precondition: l is a list with comparable elements

    Parameter step_list: The list to contain steps of the sort. They represent
    any changes made at a given step, a tuple of (origin index, new index)
    Precondition: step_list is a list
    """
    l=l[:]
    highest = len(l) - 1
    lowest = 0
    while highest > 0:
        swaps = 0
        for i in range(lowest,highest):
            if l[i] > l[i+1]:
                l.insert(i+1,l.pop(i))
                s_list.append((i,i+1))
                swaps+=1
            else:
                s_list.append((i,i))
        if swaps == 0:
            break
        for i in range(highest-1,lowest-1,-1):
            if l[i] < l[i-1]:
                l.insert(i-1 if i != 0 else 0,l.pop(i))
                s_list.append((i,i-1 if i != 0 else 0))
                swaps+=1
            else:
                s_list.append((i,i))
        highest -= 1
        lowest += 1
        if swaps == 0:
            break
    return l


algos = {'quicksort': step_quicksort,
        'mergesort': step_mergesort,
        'bubblesort': step_bubblesort,
        'cocktail shaker sort': step_cocktail_shaker,
        'insertion sort': step_insertion_sort,
        'selection sort': step_selection_sort}
