import timeit
import random


def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


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
        while j >= 0 and k < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
    left = merge_sort(left)
    right = merge_sort(right)

    def _merge(l, r):
        result = []
        while l and r:
            result.append(l.pop(0)) if l[0] <= r[0] else result.append(r.pop(0))
        while l:
            result += l
        while r:
            result += r
        return result

    return _merge(left, right)

# Default python sorting algorithm
def tim_sort(arr):
    pass


def main():
  pass


def test(arr):
    def _insertion(a):
        return str(insertion_sort(a) == sorted(a))
    def _quick(a):
        return str(quick_sort(a) == sorted(a))
    def _bubble(a):
        return str(bubble_sort(a) == sorted(a))
    return "Insertion: " + _insertion(arr.copy()) + "\nQuick: " + _quick(arr.copy()) + "\nBubble: " + _bubble(arr.copy())

if __name__ == '__main__':
    strings = ["hey", "zed", "inhumane", "a", "c", "b", "z", "p"]
    ints = [int(1000*random.random()) for i in range(500)]
    print(test(ints))
    qsort = timeit.Timer(lambda: quick_sort(ints.copy()))
    print("Quick sort: " + format(qsort.timeit(10), '.20f') + " seconds")
    print(ints)

    isort = timeit.Timer(lambda: insertion_sort((ints.copy())))
    print("Insertion sort: " + format(isort.timeit(10), '.20f') + " seconds")
    print(ints)

    bsort = timeit.Timer(lambda: bubble_sort(ints.copy()))
    print("Bubble sort:" + format(bsort.timeit(10), '.20f') + " seconds")
    print(ints)

    print(merge_sort(ints.copy()) == sorted(ints))

