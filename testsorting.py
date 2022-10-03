"""
A script for testing the sorting module

Author: Jacob Dentes
Date: 13 October 2021
"""
import sorting

def test(fun, list):
    """
    Tests a sorting algorithm and its sorting steps.

    Tests the algorithm against the built-in sorted() function, tests the
    sorting steps by executing them.

    Parameter fun: The sorting function to execute
    Precondition: fun is a function that returns a copy of a list sorted with
    the first parameter taking a list to sort and the second parameter being
    a list to modify in place with the sorting steps

    Parameter list: The list to test the sorting algorithm on
    Precondition: list is a list of all comparable items.
    """
    x = []
    list = list[:]
    l = fun(list[:], x)
    real = sorted(list)
    assert l == real, f'Sorted incorrectly, expected {real}, got {l}'
    for step in x:
        list.insert(step[1],list.pop(step[0]))
    assert list == real,f'Incorrect steps {x} produced {list} instead of {real}'

def main():
    print('Testing quicksort')
    # Testing a generic case
    test(sorting.step_quicksort, [3,8,6,4])
    # Testing a case with repetition
    test(sorting.step_quicksort, [3,8,8,6,4])
    # Testing a case with negatives
    test(sorting.step_quicksort, [-20,2,8,6,4])
    # Testing a case with only negatives
    test(sorting.step_quicksort, [-3,-8,-9,-6,-4])
    # Testing a case with zeros
    test(sorting.step_quicksort, [3,8,0,6,4])
    # Testing a case with only repetition
    test(sorting.step_quicksort, [2,2,2,2])
    # Testing a case that is already sorted
    test(sorting.step_quicksort, [1,2,3,4,5])
    # Testing a case with non-numbers
    test(sorting.step_quicksort, ['a','z','q','p'])

    print('Testing mergesort')
    # Testing a generic case
    test(sorting.step_mergesort, [3,8,6,4])
    # Testing a case with repetition
    test(sorting.step_mergesort, [3,8,8,6,4])
    # Testing a case with negatives
    test(sorting.step_mergesort, [-20,2,8,6,4])
    # Testing a case with only negatives
    test(sorting.step_mergesort, [-3,-8,-9,-6,-4])
    # Testing a case with zeros
    test(sorting.step_mergesort, [3,8,0,6,4])
    # Testing a case with only repetition
    test(sorting.step_mergesort, [2,2,2,2])
    # Testing a case that is already sorted
    test(sorting.step_mergesort, [1,2,3,4,5])
    # Testing a case with non-numbers
    test(sorting.step_mergesort, ['a','z','q','p'])

    print('Testing bubblesort')
    # Testing a generic case
    test(sorting.step_bubblesort, [3,8,6,4])
    # Testing a case with repetition
    test(sorting.step_bubblesort, [3,8,8,6,4])
    # Testing a case with negatives
    test(sorting.step_bubblesort, [-20,2,8,6,4])
    # Testing a case with only negatives
    test(sorting.step_bubblesort, [-3,-8,-9,-6,-4])
    # Testing a case with zeros
    test(sorting.step_bubblesort, [3,8,0,6,4])
    # Testing a case with only repetition
    test(sorting.step_bubblesort, [2,2,2,2])
    # Testing a case that is already sorted
    test(sorting.step_bubblesort, [1,2,3,4,5])
    # Testing a case with non-numbers
    test(sorting.step_bubblesort, ['a','z','q','p'])

    print('Testing insertion sort')
    # Testing a generic case
    test(sorting.step_insertion_sort, [3,8,6,4])
    # Testing a case with repetition
    test(sorting.step_insertion_sort, [3,8,8,6,4])
    # Testing a case with negatives
    test(sorting.step_insertion_sort, [-20,2,8,6,4])
    # Testing a case with only negatives
    test(sorting.step_insertion_sort, [-3,-8,-9,-6,-4])
    # Testing a case with zeros
    test(sorting.step_insertion_sort, [3,8,0,6,4])
    # Testing a case with only repetition
    test(sorting.step_insertion_sort, [2,2,2,2])
    # Testing a case that is already sorted
    test(sorting.step_insertion_sort, [1,2,3,4,5])
    # Testing a case with non-numbers
    test(sorting.step_insertion_sort, ['a','z','q','p'])

    print('Testing selection sort')
    # Testing a generic case
    test(sorting.step_selection_sort, [3,8,6,4])
    # Testing a case with repetition
    test(sorting.step_selection_sort, [3,8,8,6,4])
    # Testing a case with negatives
    test(sorting.step_selection_sort, [-20,2,8,6,4])
    # Testing a case with only negatives
    test(sorting.step_selection_sort, [-3,-8,-9,-6,-4])
    # Testing a case with zeros
    test(sorting.step_selection_sort, [3,8,0,6,4])
    # Testing a case with only repetition
    test(sorting.step_selection_sort, [2,2,2,2])
    # Testing a case that is already sorted
    test(sorting.step_selection_sort, [1,2,3,4,5])
    # Testing a case with non-numbers
    test(sorting.step_selection_sort, ['a','z','q','p'])

    print('Testing cocktail shaker sort')
    # Testing a generic case
    test(sorting.step_cocktail_shaker, [3,8,6,4])
    # Testing a case with repetition
    test(sorting.step_cocktail_shaker, [3,8,8,6,4])
    # Testing a case with negatives
    test(sorting.step_cocktail_shaker, [-20,2,8,6,4])
    # Testing a case with only negatives
    test(sorting.step_cocktail_shaker, [-3,-8,-9,-6,-4])
    # Testing a case with zeros
    test(sorting.step_cocktail_shaker, [3,8,0,6,4])
    # Testing a case with only repetition
    test(sorting.step_cocktail_shaker, [2,2,2,2])
    # Testing a case that is already sorted
    test(sorting.step_cocktail_shaker, [1,2,3,4,5])
    # Testing a case with non-numbers
    test(sorting.step_cocktail_shaker, ['a','z','q','p'])

    print('Module passed all tests')


if __name__ == '__main__':
    main()
