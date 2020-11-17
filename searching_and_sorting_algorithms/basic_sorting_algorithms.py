from searching_and_sorting_algorithms.sorting_helping_methods import swap_positions

'''
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray
is picked and moved to the sorted subarray.
'''


def selection_sort(array_to_be_sorted: list) -> list:
    for i in range(len(array_to_be_sorted)):
        for j in range(i + 1, len(array_to_be_sorted)):
            if array_to_be_sorted[j] < array_to_be_sorted[i]:
                swap_positions(array_to_be_sorted, j, i)

    return array_to_be_sorted


'''
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if
they are in wrong order.
'''


def bubble_sort(my_array):
    for i in range(len(my_array) - 1):
        for j in range(len(my_array) - i - 1):
            if my_array[j + 1] < my_array[j]:
                swap_positions(my_list, j, j + 1)

    return my_array

'''
Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted,
 only few elements are misplaced in complete big array.
'''


def insertion_sort(my_array: list):
    for i in range(1, len(my_array)):
        j = i - 1
        while j >= 0 and my_array[j] > my_array[i]:
            swap_positions(my_list, i, j)
            j -= 1
            i -= 1
    return my_array


my_list = [9, 4, 6, 3, 25, 11, 1, 3]
print('Unsorted array ', my_list)
# print('Selection sort', selection_sort(my_list))
# print('Bubble sort', bubble_sort(my_list))
# print('Insertion sort', insertion_sort(my_list))
