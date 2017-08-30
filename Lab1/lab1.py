import timeit
import random


def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j], arr[j+1] = arr[j+1], temp


def quick_sort(arr):
    if not arr:
        return arr
    pivot = arr[0]
    below = [i for i in arr[1:] if i < pivot]
    above = [i for i in arr[1:] if i >= pivot]
    return quick_sort(below) + [pivot] + quick_sort(above)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0  and k < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k


def merge_sort(arr):
    pass


def rand_sort(arr):
    pass

if __name__ == '__main__':
    strings = ["hey", "zed", "inhumane", "a", "c", "b", "z", "p"]
    ints = [int(1000*random.random()) for i in range(50)]

    qsort = timeit.Timer(lambda: quick_sort(ints))
    print("Quick sort: " + format(qsort.timeit(10), '.20f') + " seconds")
    print(ints)

    isort = timeit.Timer(lambda: insertion_sort((ints)))
    print("Insertion sort: " + format(isort.timeit(10), '.20f') + " seconds")
    print(ints)

    bsort = timeit.Timer(lambda: bubble_sort(ints))
    print("Bubble sort:" + format(bsort.timeit(10), '.20f') + " seconds")
    print(ints)


