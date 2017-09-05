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

    return merge(left, right)


def merge(l, r):
    result = []
    while l and r:
        result.append(l.pop(0)) if l[0] <= r[0] else result.append(r.pop(0))
    result = result + l if l else result + r
    return result


# Default python sorting algorithm
def tim_sort(arr):
    pass


def timer(arr, algo):
    sort = timeit.Timer(lambda: globals()[algo](arr.copy()))
    print(algo + ": " + format(sort.timeit(10), '.20f') + " seconds")

def main():
  pass


def test(arr):
    def _insertion(a):
        insertion_sort(a)
        return str(a == sorted(a))

    def _quick(a):
        return str(sorted(a) == quick_sort(a))

    def _bubble(a):
        bubble_sort(a)
        return str(sorted(a) == a)

    def _merge(a):
        return str(sorted(a) == merge_sort(a))

    def _tim(a):
        return
    return "Insertion: " + _insertion(arr.copy()) + \
           "\nQuick: " + _quick(arr.copy()) + \
           "\nBubble: " + _bubble(arr.copy()) + \
           "\nMerge: " + _merge(arr.copy()) + \
           "\nTim: " + _tim(arr.copy())

if __name__ == '__main__':
    strings = ["hey", "zed", "inhumane", "a", "c", "b", "z", "p"]
    ints = [int(1000*random.random()) for i in range(10)]

    timer(ints, "quick_sort")
    timer(ints, "merge_sort")
    timer(ints, "insertion_sort")
    timer(ints, "bubble_sort")
    print(test(ints))
