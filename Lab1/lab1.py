import timeit
import random


def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j], arr[j+1] = arr[j+1], temp


def quick_sort(arr):
    pass


def insertion_sort(arr):
    pass


def merge_sort(arr):
    pass


def rand_sort(arr):
    pass

if __name__ == '__main__':
    strings = ["hey", "zed", "inhumane", "a", "c", "b", "z", "p"]
    ints = [int(1000*random.random()) for i in range(100)]
    t = timeit.Timer(lambda: bubble_sort(ints))
    print(format(t.timeit(10), '.20f') + " seconds")
    print(ints)
